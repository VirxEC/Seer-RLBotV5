from rlbot.flat import AirState, FieldInfo, GamePacket, PlayerInfo, ControllerState, MatchPhase

from bot import MyBot
from typing import Dict

import numpy as np
import math


from kickoff_data import *

from typing import Union

SIDE_WALL_X = 4096  # +/-
BACK_WALL_Y = 5120  # +/-
CEILING_Z = 2044
BACK_NET_Y = 6000  # +/-

GOAL_HEIGHT = 642.775
GOAL_CENTER_TO_POST = 892.755
ORANGE_GOAL_CENTER = (0, BACK_WALL_Y, GOAL_HEIGHT / 2)
BLUE_GOAL_CENTER = (0, -BACK_WALL_Y, GOAL_HEIGHT / 2)


KICKOFF_POS_BLUE = [
    [-2048, -2560],
    [2048, -2560],
    [-256.0, -3840],
    [256.0, -3840],
    [0.0, -4608],
]

KICKOFF_POS_ORANGE = [
    [2048, 2560],
    [-2048, 2560],
    [256.0, 3840],
    [-256.0, 3840],
    [0.0, 4608],
]


class Vec3:
    """
    This class should provide you with all the basic vector operations that you need, but feel free to extend its
    functionality when needed.
    The vectors found in the GamePacket will be flatbuffer vectors. Cast them to Vec3 like this:
    `car_location = Vec3(car.physics.location)`.

    Remember that the in-game axis are left-handed.

    When in doubt visit the wiki: https://github.com/RLBot/RLBot/wiki/Useful-Game-Values
    """
    # https://docs.python.org/3/reference/datamodel.html#slots
    __slots__ = [
        'x',
        'y',
        'z'
    ]

    def __init__(self, x: Union[float, 'Vec3', ] = 0, y: float = 0, z: float = 0):
        """
        Create a new Vec3. The x component can alternatively be another vector with an x, y, and z component, in which
        case the created vector is a copy of the given vector and the y and z parameter is ignored. Examples:

        a = Vec3(1, 2, 3)

        b = Vec3(a)

        """

        if hasattr(x, 'x'):
            # We have been given a vector. Copy it
            self.x = float(x.x)
            self.y = float(x.y) if hasattr(x, 'y') else 0
            self.z = float(x.z) if hasattr(x, 'z') else 0
        else:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)

    def __getitem__(self, item: int):
        return (self.x, self.y, self.z)[item]

    def __add__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __mul__(self, scale: float) -> 'Vec3':
        return Vec3(self.x * scale, self.y * scale, self.z * scale)

    def __rmul__(self, scale):
        return self * scale

    def __truediv__(self, scale: float) -> 'Vec3':
        scale = 1 / float(scale)
        return self * scale

    def __str__(self):
        return f"Vec3({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    def __repr__(self):
        return self.__str__()

    def flat(self):
        """Returns a new Vec3 that equals this Vec3 but projected onto the ground plane. I.e. where z=0."""
        return Vec3(self.x, self.y, 0)

    def length(self):
        """Returns the length of the vector. Also called magnitude and norm."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dist(self, other: 'Vec3') -> float:
        """Returns the distance between this vector and another vector using pythagoras."""
        return (self - other).length()

    def normalized(self):
        """Returns a vector with the same direction but a length of one."""
        return self / self.length()

    def rescale(self, new_len: float) -> 'Vec3':
        """Returns a vector with the same direction but a different length."""
        return new_len * self.normalized()

    def dot(self, other: 'Vec3') -> float:
        """Returns the dot product."""
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other: 'Vec3') -> 'Vec3':
        """Returns the cross product."""
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def ang_to(self, ideal: 'Vec3') -> float:
        """Returns the angle to the ideal vector. Angle will be between 0 and pi."""
        cos_ang = self.dot(ideal) / (self.length() * ideal.length())
        return math.acos(cos_ang)


class Orientation:
    """
    This class describes the orientation of an object from the rotation of the object.
    Use this to find the direction of cars: forward, right, up.
    It can also be used to find relative locations.
    """

    def __init__(self, rotation):
        self.yaw = float(rotation.yaw)
        self.roll = float(rotation.roll)
        self.pitch = float(rotation.pitch)

        cr = math.cos(self.roll)
        sr = math.sin(self.roll)
        cp = math.cos(self.pitch)
        sp = math.sin(self.pitch)
        cy = math.cos(self.yaw)
        sy = math.sin(self.yaw)

        self.forward = Vec3(cp * cy, cp * sy, sp)
        self.right = Vec3(cy*sp*sr-cr*sy, sy*sp*sr+cr*cy, -cp*sr)
        self.up = Vec3(-cr*cy*sp-sr*sy, -cr*sy*sp+sr*cy, cp*cr)


# Sometimes things are easier, when everything is seen from your point of view.
# This function lets you make any location the center of the world.
# For example, set center to your car's location and ori to your car's orientation, then the target will be
# relative to your car!
def relative_location(center: Vec3, ori: Orientation, target: Vec3) -> Vec3:
    """
    Returns target as a relative location from center's point of view, using the given orientation. The components of
    the returned vector describes:

    * x: how far in front
    * y: how far right
    * z: how far above
    """
    x = (target - center).dot(ori.forward)
    y = (target - center).dot(ori.right)
    z = (target - center).dot(ori.up)
    return Vec3(x, y, z)


def limit_to_safe_range(value: float) -> float:
    """
    Controls like throttle, steer, pitch, yaw, and roll need to be in the range of -1 to 1.
    This will ensure your number is in that range. Something like 0.45 will stay as it is,
    but a value of -5.6 would be changed to -1.
    """
    if value < -1:
        return -1
    if value > 1:
        return 1
    return value


def steer_toward_target(car, target) -> float:
    relative = relative_location(Vec3(car.physics.location), Orientation(car.physics.rotation), target)
    angle = math.atan2(relative.y, relative.x)
    return limit_to_safe_range(angle * 5)


def _vector_to_numpy(vector):
    return np.asarray([vector.x, vector.y, vector.z])


class LeBotKickoffs(MyBot):
    def __init__(self, default_agent_id: str | None = None):
        super().__init__(default_agent_id)

        self.current_kickoff = LearnedKickoff()
        self.kickoff_player = None

    def get_kickoff_player(self, packet: GamePacket):
        pos = None

        if self.team == 0:  # BLUE
            pos = [2048.0, -2560.0, 17.0]
        elif self.team == 1:  # ORANGE
            pos = [-2048.0, 2560.0, 17.0]
        else:
            raise NotImplementedError(self.team)

        players = []
        for p in packet.players:
            if p.team == self.team:
                players.append(p)

        players = [(i, np.linalg.norm(_vector_to_numpy(i.physics.location) -
                    _vector_to_numpy(packet.balls[0].physics.location))) for i in players]
        players = sorted(players, key=lambda x: x[1])
        shortest_dist = players[0][1]

        players = list(filter(lambda x: x[1] - shortest_dist < 1e-4, players))
        players = [x[0] for x in players]

        players = [(i, np.linalg.norm(_vector_to_numpy(
            i.physics.location) - np.array(pos))) for i in players]
        players = sorted(players, key=lambda x: x[1])

        kickoff_player = players[0][0]

        return kickoff_player

    def get_kickoff_type(self, packet: GamePacket, kickoff_player):

        for i in range(len(KICKOFF_POS_BLUE)):

            if kickoff_player.physics.location.x == KICKOFF_POS_BLUE[i][0] and kickoff_player.physics.location.y == KICKOFF_POS_BLUE[i][1] \
                    or kickoff_player.physics.location.x == KICKOFF_POS_ORANGE[i][0] and kickoff_player.physics.location.y == KICKOFF_POS_ORANGE[i][1]:
                return i

        # raise NotImplementedError(kickoff_player)
        return 0

    def choose_kickoff(self, packet: GamePacket, kickoff_player):
        kickoff_type = self.get_kickoff_type(packet, kickoff_player)

        if len(packet.players) == 2:
            kickoffs = KICKOFFS_1v1
        elif len(packet.players) == 4:
            kickoffs = KICKOFFS_2v2
        else:
            kickoffs = KICKOFFS_3v3

        kickoffs_classes = [a[1] for a in kickoffs[kickoff_type]]
        p = np.array([a[0] for a in kickoffs[kickoff_type]])
        p = p / np.sum(p)

        return np.random.choice(kickoffs_classes, p=p)

    def get_outputs(self, packet: GamePacket) -> Dict[int, ControllerState]:

        parent_actions = super().get_outputs(packet)

        if len(packet.balls) > 0 and packet.balls[0].physics.location.x == 0.0 and packet.match_info.match_phase == MatchPhase.Countdown:
            self.kickoff_player = self.get_kickoff_player(packet)
            self.current_kickoff = self.choose_kickoff(packet, self.kickoff_player)
            self.current_kickoff.reset()

        if self.current_kickoff.is_done():
            return parent_actions
        else:
            return self.current_kickoff.get_actions(packet, parent_actions, self.kickoff_player)


class Kickoff:
    def __init__(self) -> None:
        pass

    def is_done(self,):
        return False

    def reset(self):
        pass

    def get_kickoff_player_index(self, packet: GamePacket, kickoff_player):
        for i, car in enumerate(packet.players):
            if car.name == kickoff_player.name:
                return i
        raise NotImplementedError(kickoff_player)

    def get_actions(self, packet: GamePacket, parent_actions, kickoff_player):
        return parent_actions


class LearnedKickoff(Kickoff):

    def is_done(self):
        return True

    def get_actions(self, packet: GamePacket, parent_actions, kickoff_player):
        return parent_actions


class HardcodedKickoffDouble(Kickoff):
    def __init__(self, sequence_main, sequence_cheater) -> None:
        super().__init__()
        self.sequence_main = sequence_main
        self.sequence_cheater = sequence_cheater
        self.index = 0


    def reset(self):
        self.index = 0

    def is_done(self):
        return self.index >= len(self.sequence_main)

    def get_actions(self, packet: GamePacket, parent_actions, kickoff_player):

        kickoff_player_index = self.get_kickoff_player_index(
            packet, kickoff_player)

        actions = {}
        for key in parent_actions:

            if key == kickoff_player_index:
                actions[key] = self.sequence_main[self.index]
            else:
                actions[key] = self.sequence_cheater[self.index]

        self.index += 1
        return actions


class SpanishKickoff(Kickoff):
    def __init__(self, sequence_main, sequence_cheater) -> None:
        super().__init__()
        self.sequence_main = sequence_main
        self.sequence_cheater = sequence_cheater
        self.index_main = 0
        self.index_cheater = 0

        self.done = False

        self.chase_counter = 0

    def reset(self):
        self.index_main = 0
        self.index_cheater = 0
        self.done = False
        self.chase_counter

    def is_done(self):
        return self.done

    def get_actions(self, packet, parent_actions, kickoff_player):

        kickoff_player_index = self.get_kickoff_player_index(packet, kickoff_player)

        actions = {}
        for key in parent_actions:

            if key == kickoff_player_index:

                if self.index_main < len(self.sequence_main):
                    actions[key] = self.sequence_main[self.index_main]
                    self.index_main += 1
                else:

                    self.chase_counter += 1
                    opponent_goal = None
                    if packet.game_cars[key].team == 0:  # Blue
                        opponent_goal = ORANGE_GOAL_CENTER
                    else:
                        opponent_goal = BLUE_GOAL_CENTER

                    opponents = []

                    for cars in packet.players:
                        if cars.team != packet.players[key].team:
                            opponents.append(cars)

                    goal_distances = [np.linalg.norm(_vector_to_numpy(
                        car.physics.location) - np.array(opponent_goal)) for car in opponents]

                    min_distance = np.min(goal_distances)

                    target = None

                    for i, d in enumerate(goal_distances):
                        if d == min_distance:
                            target = opponents[i]
                            break


                    p1 = np.array([packet.game_cars[key].physics.location.x, packet.game_cars[key].physics.location.y])
                    v1 = np.array([packet.game_cars[key].physics.velocity.x, packet.game_cars[key].physics.velocity.y])
                    p2 = np.array([target.physics.location.x, target.physics.location.y])
                    v2 = np.array([target.physics.velocity.x, target.physics.velocity.y])

                    p_rel = p1 - p2
                    v_rel = v1-v2

                    t_collision = np.linalg.norm(p_rel) / np.linalg.norm(v_rel)

                    solution = p2 + t_collision * v2

                    input = ControllerState()
                    input.throttle = 1.0
                    input.steer = steer_toward_target(packet.game_cars[key], Vec3(solution[0], solution[1], 17.5))

                    current_player_speed = np.linalg.norm(_vector_to_numpy(packet.game_cars[key].physics.velocity))
                    if current_player_speed < 2200:
                        input.boost = True

                    if current_player_speed < 2200 and packet.game_cars[key].boost == 0:
                        self.done = True

                    if target.is_demolished:
                        self.done = True

                    if self.chase_counter > 5*120:
                        self.done = True

                    if target.jumped:
                        self.done = True

                    actions[key] = input

            else:
                if self.index_cheater < len(self.sequence_cheater):
                    actions[key] = self.sequence_cheater[self.index_cheater]
                    self.index_cheater += 1
                else:
                    actions[key] = parent_actions[key]

        return actions


class FakeSpanishKickoff(Kickoff):
    def __init__(self, sequence) -> None:
        super().__init__()
        self.sequence = sequence
        self.index = 0

    def reset(self):
        self.index = 0

    def is_done(self):
        return self.index >= len(self.sequence)

    def get_actions(self, packet: GamePacket, parent_actions, kickoff_player):

        actions = {}

        kickoff_player_index = self.get_kickoff_player_index(packet, kickoff_player)

        for key in parent_actions:

            if key == kickoff_player_index:
                actions[key] = parent_actions[key]
            else:
                actions[key] = self.sequence[self.index]
                self.index += 1

        return actions


class HardcodedKickoffSingle(Kickoff):
    def __init__(self, sequence) -> None:
        super().__init__()
        self.sequence = sequence
        self.index = 0

    def reset(self):
        self.index = 0

    def is_done(self):
        return self.index >= len(self.sequence)

    def get_actions(self, packet: GamePacket, parent_actions, kickoff_player):

        kickoff_player_index = self.get_kickoff_player_index(
            packet, kickoff_player)
        parent_actions[kickoff_player_index] = self.sequence[self.index]
        self.index += 1
        return parent_actions


RIGHT_DIAG_KICKOFFS_2v2 = [
    (0.16, HardcodedKickoffSingle(RIGHT_DIAG_KICKOFF_SPEEDFLIP)),
    (0.16, HardcodedKickoffSingle(RIGHT_DIAG_KICKOFF_FAKE)),
    (0.16, HardcodedKickoffSingle(SIMPLE_FRONTFLIP)),
    (0.5, LearnedKickoff()),
]


LEFT_DIAG_KICKOFFS_2v2 = [
    (0.16, HardcodedKickoffSingle(LEFT_DIAG_KICKOFF_SPEEDFLIP)),
    (0.16, HardcodedKickoffSingle(LEFT_DIAG_KICKOFF_FAKE)),
    (0.16, HardcodedKickoffSingle(SIMPLE_FRONTFLIP)),
    (0.5, LearnedKickoff()),
]


RIGHT_MID_KICKOFFS_2v2 = [
    (0.1, HardcodedKickoffSingle(RIGHT_MID_KICKOFF_SPEEDFLIP)),
    (0.2, SpanishKickoff(RIGHT_MID_KICKOFF_FAKE_SPANISH, RIGHT_MID_KICKOFF_FAKE_CHEATER)),
    (0.1, HardcodedKickoffDouble(RIGHT_MID_KICKOFF_FAKE, RIGHT_MID_KICKOFF_FAKE_CHEATER)),
    (0.1, HardcodedKickoffSingle(RIGHT_MID_SIMPLE_DELAYED)),
    (0.4, LearnedKickoff()),
    (0.1, FakeSpanishKickoff(RIGHT_MID_KICKOFF_FAKE_CHEATER))
]


LEFT_MID_KICKOFFS_2v2 = [
    (0.1, HardcodedKickoffSingle(LEFT_MID_KICKOFF_SPEEDFLIP)),
    (0.2, SpanishKickoff(LEFT_MID_KICKOFF_FAKE_SPANISH, LEFT_MID_KICKOFF_FAKE_CHEATER)),
    (0.1, HardcodedKickoffDouble(LEFT_MID_KICKOFF_FAKE, LEFT_MID_KICKOFF_FAKE_CHEATER)),
    (0.1, HardcodedKickoffSingle(LEFT_MID_SIMPLE_DELAYED)),
    (0.4, LearnedKickoff()),
    (0.1, FakeSpanishKickoff(LEFT_MID_KICKOFF_FAKE_CHEATER))
]


KICKOFFS_2v2 = [
    RIGHT_DIAG_KICKOFFS_2v2,
    LEFT_DIAG_KICKOFFS_2v2,
    RIGHT_MID_KICKOFFS_2v2,
    LEFT_MID_KICKOFFS_2v2,
]

RIGHT_DIAG_KICKOFFS_1v1 = [
    (0.15, HardcodedKickoffSingle(RIGHT_DIAG_KICKOFF_SPEEDFLIP)),
    (0.15, HardcodedKickoffSingle(RIGHT_DIAG_KICKOFF_FAKE)),
    (0.3, HardcodedKickoffSingle(SIMPLE_FRONTFLIP)),
    (0.4, LearnedKickoff()),
]

LEFT_DIAG_KICKOFFS_1v1 = [
    (0.15, HardcodedKickoffSingle(LEFT_DIAG_KICKOFF_SPEEDFLIP)),
    (0.15, HardcodedKickoffSingle(LEFT_DIAG_KICKOFF_FAKE)),
    (0.3, HardcodedKickoffSingle(SIMPLE_FRONTFLIP)),
    (0.4, LearnedKickoff()),
]

RIGHT_MID_KICKOFFS_1v1 = [
    (0.25, HardcodedKickoffSingle(RIGHT_MID_KICKOFF_SPEEDFLIP)),
    (0.25, HardcodedKickoffSingle(RIGHT_MID_SIMPLE_DELAYED)),
    (0.5, LearnedKickoff()),
]


LEFT_MID_KICKOFFS_1v1 = [
    (0.25, HardcodedKickoffSingle(LEFT_MID_KICKOFF_SPEEDFLIP)),
    (0.25, HardcodedKickoffSingle(LEFT_MID_SIMPLE_DELAYED)),
    (0.5, LearnedKickoff()),
]

MID_KICKOFFS_1v1 = [
    (0.4, HardcodedKickoffSingle(MID_KICKOFF_SPEEDFLIP)),
    (0.3, HardcodedKickoffSingle(MID_SIMPLE_DELAYED)),
    (0.3, LearnedKickoff())
]


KICKOFFS_1v1 = [
    RIGHT_DIAG_KICKOFFS_1v1,
    LEFT_DIAG_KICKOFFS_1v1,
    RIGHT_MID_KICKOFFS_1v1,
    LEFT_MID_KICKOFFS_1v1,
    MID_KICKOFFS_1v1
]





LEFT_MID_KICKOFFS_3v3 = [
    (0.25, HardcodedKickoffSingle(LEFT_MID_KICKOFF_SPEEDFLIP)),
    (0.25, HardcodedKickoffSingle(LEFT_MID_SIMPLE_DELAYED)),
    (0.5, LearnedKickoff()),
]


RIGHT_DIAG_KICKOFFS_3v3 = [
    (0.15, HardcodedKickoffSingle(RIGHT_DIAG_KICKOFF_SPEEDFLIP)),
    (0.15, HardcodedKickoffSingle(RIGHT_DIAG_KICKOFF_FAKE)),
    (0.3, HardcodedKickoffSingle(SIMPLE_FRONTFLIP)),
    (0.4, LearnedKickoff()),
]

LEFT_DIAG_KICKOFFS_3v3 = [
    (0.15, HardcodedKickoffSingle(LEFT_DIAG_KICKOFF_SPEEDFLIP)),
    (0.15, HardcodedKickoffSingle(LEFT_DIAG_KICKOFF_FAKE)),
    (0.3, HardcodedKickoffSingle(SIMPLE_FRONTFLIP)),
    (0.4, LearnedKickoff()),
]


KICKOFFS_3v3 = [
    RIGHT_DIAG_KICKOFFS_3v3,
    LEFT_DIAG_KICKOFFS_3v3,
    LEFT_MID_KICKOFFS_3v3,
    LEFT_MID_KICKOFFS_3v3,
]
# Note: LEFT_MID_KICKOFFS_3v3 should be at index 3


if __name__ == "__main__":
    LeBotKickoffs("ultrawidegc/lebot").run()
