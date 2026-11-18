from rlbot.flat import ControllerState

RIGHT_DIAG_KICKOFF_SPEEDFLIP = (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 4 * 4 * [ControllerState(throttle=1, boost=True, steer=1)]
        + 1 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=-0.7, pitch=-0.8, jump=True, boost=True)]
        + 13 * 4 * [ControllerState(throttle=1, roll=-0.5, pitch=1, boost=True, handbrake=True)]
        + 10 * 4 * [ControllerState(throttle=1, roll=-1, pitch=0.5, handbrake=True)]
)

SIMPLE_FRONTFLIP = (
        10 * 4 * [ControllerState(throttle=1, boost=True)]
        + 4 * 4 * [ControllerState(throttle=1)]
        + 2 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, pitch=-1, jump=True, boost=True)]
        + 14 * 4 * [ControllerState(throttle=1, handbrake=True)]
)


LEFT_DIAG_KICKOFF_SPEEDFLIP = (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 4 * 4 * [ControllerState(throttle=1, boost=True, steer=-1)]
        + 1 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=0.7, pitch=-0.8, jump=True, boost=True)]
        + 13 * 4 * [ControllerState(throttle=1, roll=0.5, pitch=1, boost=True, handbrake=True)]
        + 10 * 4 * [ControllerState(throttle=1, roll=1, pitch=0.5, handbrake=True)]
)


MID_KICKOFF_SPEEDFLIP = (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 4 * 4 * [ControllerState(throttle=1, boost=True, steer=-1)]
        + 2 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=0.8, pitch=-0.7, jump=True, boost=True)]
        + 13 * 4 * [ControllerState(throttle=1, pitch=1, boost=True, handbrake=True)]
        + 11 * 4 * [ControllerState(throttle=1, roll=1, pitch=0.5, boost=True, handbrake=True)]
)

MID_SIMPLE_DELAYED = (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 4 * 4 * [ControllerState(throttle=1, boost=True, steer=-1)]
        + 2 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=False)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=0.8, pitch=-0.7, jump=True, boost=False)]
        + 13 * 4 * [ControllerState(throttle=1, pitch=1, boost=False, handbrake=True)]
        + 11 * 4 * [ControllerState(throttle=1, roll=1, pitch=0.5, boost=False, handbrake=True)]
)


helper_fake_left = [
ControllerState(throttle=-1.0, steer=0.0, pitch=0.7960753440856934, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-1.0, steer=0.0, pitch=0.8274483680725098, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-0.9607837200164795, steer=0.0, pitch=0.8588213920593262, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-0.8196051120758057, steer=0.0, pitch=0.8745079040527344, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-0.6980345845222473, steer=0.0, pitch=0.8745079040527344, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-0.6078371405601501, steer=0.0, pitch=0.8745079040527344, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-0.4901883006095886, steer=0.0, pitch=0.8666646480560303, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=-0.3097933828830719, steer=0.0, pitch=0.8588213920593262, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=-0.12939848005771637, steer=0.21567431092262268, pitch=0.843134880065918, yaw=0.21567431092262268, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.23920407891273499, pitch=0.8352916240692139, yaw=0.23920407891273499, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=0.8352916240692139, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=0.843134880065918, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=0.8588213920593262, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=0.8745079040527344, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=0.8901944160461426, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=0.9058809280395508, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=0.9372539520263672, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.0, pitch=1.0, yaw=0.0, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.14508499205112457, pitch=1.0, yaw=0.14508499205112457, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.2862636148929596, pitch=1.0, yaw=0.2862636148929596, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.14508499205112457, pitch=1.0, yaw=0.14508499205112457, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.19214454293251038, pitch=1.0, yaw=0.19214454293251038, roll=0.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.23920407891273499, pitch=1.0, yaw=0.23920407891273499, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.2627338469028473, pitch=1.0, yaw=0.2627338469028473, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.2705771028995514, pitch=1.0, yaw=0.2705771028995514, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.2784203588962555, pitch=1.0, yaw=0.2784203588962555, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.2548905909061432, pitch=1.0, yaw=0.2548905909061432, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=0.20783105492591858, pitch=0.8274483680725098, yaw=0.20783105492591858, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.14508499205112457, steer=0.13724173605442047, pitch=0.5686208605766296, yaw=0.13724173605442047, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.21959593892097473, steer=0.0, pitch=0.2862636148929596, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.3019501268863678, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.3960692286491394, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.43920713663101196, steer=0.0, pitch=0.0, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.4823450446128845, steer=0.0, pitch=-0.12942899763584137, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.5529343485832214, steer=0.0, pitch=-0.23923459649085999, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.6156803965568542, steer=0.0, pitch=-0.3568834364414215, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.6784264445304871, steer=0.0, pitch=-0.4745323061943054, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.8039186000823975, steer=0.0, pitch=-0.6235541701316833, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.8509781360626221, steer=0.0, pitch=-0.7333597540855408, yaw=0.0, roll=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.9098025560379028, steer=-0.20001831650733948, pitch=-0.9137547016143799, yaw=-0.20001831650733948, roll=1.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.9568620920181274, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=1.0, steer=-0.10589922964572906, pitch=-1.0, yaw=-0.10589922964572906, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.12942899763584137, pitch=-1.0, yaw=-0.12942899763584137, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.12158574163913727, pitch=-1.0, yaw=-0.12158574163913727, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.12158574163913727, pitch=-1.0, yaw=-0.12158574163913727, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.12158574163913727, pitch=-1.0, yaw=-0.12158574163913727, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.11374248564243317, pitch=-1.0, yaw=-0.11374248564243317, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.11374248564243317, pitch=-1.0, yaw=-0.11374248564243317, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.10589922964572906, pitch=-1.0, yaw=-0.10589922964572906, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.2862941324710846, pitch=-1.0, yaw=-0.2862941324710846, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.2941373884677887, pitch=-1.0, yaw=-0.2941373884677887, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.3019806444644928, pitch=-1.0, yaw=-0.3019806444644928, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.23139134049415588, pitch=-1.0, yaw=-0.23139134049415588, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.22354808449745178, pitch=-1.0, yaw=-0.22354808449745178, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.21570482850074768, pitch=-1.0, yaw=-0.21570482850074768, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.2941373884677887, pitch=-1.0, yaw=-0.2941373884677887, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.23139134049415588, pitch=-1.0, yaw=-0.23139134049415588, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.21570482850074768, pitch=-1.0, yaw=-0.21570482850074768, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.12942899763584137, pitch=-1.0, yaw=-0.12942899763584137, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.0, pitch=-1.0, yaw=0.0, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.10589922964572906, pitch=-1.0, yaw=-0.10589922964572906, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.11374248564243317, pitch=-1.0, yaw=-0.11374248564243317, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.12158574163913727, pitch=-1.0, yaw=-0.12158574163913727, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.14511550962924957, pitch=-1.0, yaw=-0.14511550962924957, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.16864527761936188, pitch=-1.0, yaw=-0.16864527761936188, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.21570482850074768, pitch=-1.0, yaw=-0.21570482850074768, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.2549211084842682, pitch=-1.0, yaw=-0.2549211084842682, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.2784508764743805, pitch=-1.0, yaw=-0.2784508764743805, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.3490401804447174, pitch=-1.0, yaw=-0.3490401804447174, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.3960997462272644, pitch=-1.0, yaw=-0.3960997462272644, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.443159282207489, pitch=-1.0, yaw=-0.443159282207489, roll=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.4823755621910095, pitch=-1.0, yaw=-0.4823755621910095, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.52159184217453, pitch=-1.0, yaw=-0.52159184217453, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.6392406821250916, pitch=-1.0, yaw=-0.6392406821250916, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.6078676581382751, pitch=-1.0, yaw=-0.6078676581382751, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.6313974261283875, pitch=-1.0, yaw=-0.6313974261283875, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.6863002181053162, pitch=-1.0, yaw=-0.6863002181053162, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.7255164980888367, pitch=-1.0, yaw=-0.7255164980888367, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.7568895816802979, pitch=-0.9765007495880127, yaw=-0.7568895816802979, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.8039491176605225, pitch=-0.9451277256011963, yaw=-0.8039491176605225, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.8353221416473389, pitch=-0.8980681896209717, yaw=-0.8353221416473389, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.8588519096374512, pitch=-0.8666951656341553, yaw=-0.8588519096374512, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.8745384216308594, pitch=-0.8353221416473389, yaw=-0.8745384216308594, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.8902249336242676, pitch=-0.8117923736572266, yaw=-0.8902249336242676, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.9137547016143799, pitch=-0.7804193496704102, yaw=-0.9137547016143799, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.9294412136077881, pitch=-0.7568895816802979, yaw=-0.9294412136077881, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.9451277256011963, pitch=-0.7333597540855408, yaw=-0.9451277256011963, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.9529709815979004, pitch=-0.7176732420921326, yaw=-0.9529709815979004, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.9608142375946045, pitch=-0.6941434741020203, yaw=-0.9608142375946045, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.9686574935913086, pitch=-0.6784569621086121, yaw=-0.9686574935913086, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=-0.6549271941184998, yaw=-0.9921872615814209, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=-0.6313974261283875, yaw=-0.9921872615814209, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=-0.6078676581382751, yaw=-0.9921872615814209, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.5921811461448669, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.5686513781547546, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.5608081221580505, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.5451216101646423, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.5372783541679382, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.52159184217453, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.52159184217453, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.9921872615814209, pitch=-0.5059053301811218, yaw=-0.9921872615814209, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-0.9765007495880127, pitch=-0.4902188181877136, yaw=-0.9765007495880127, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4745323061943054, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4666890501976013, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4588457942008972, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4510025382041931, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4510025382041931, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.443159282207489, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4353160262107849, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4274727702140808, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4196295142173767, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4117862582206726, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4117862582206726, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4117862582206726, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4117862582206726, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4117862582206726, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4117862582206726, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4117862582206726, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4117862582206726, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=-1.0, pitch=-0.4117862582206726, yaw=-1.0, roll=0.0, jump=False, boost=True, handbrake=False),
]

helper_fake_right = [
ControllerState(throttle=-1.0,  pitch=0.7960753440856934, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-1.0,  pitch=0.8274483680725098, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-0.9607837200164795,  pitch=0.8588213920593262, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-0.8196051120758057,  pitch=0.8745079040527344, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-0.6980345845222473,  pitch=0.8745079040527344, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-0.6078371405601501,  pitch=0.8745079040527344, jump=True, boost=False, handbrake=False),
ControllerState(throttle=-0.4901883006095886,  pitch=0.8666646480560303, jump=False, boost=False, handbrake=False),
ControllerState(throttle=-0.3097933828830719,  pitch=0.8588213920593262, jump=False, boost=False, handbrake=False),
ControllerState(throttle=-0.12939848005771637, steer=-0.21567431092262268, pitch=0.843134880065918, yaw=-0.21567431092262268, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=-0.23920407891273499, pitch=0.8352916240692139, yaw=-0.23920407891273499, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=0.8352916240692139, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=0.843134880065918, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=0.8588213920593262, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=0.8745079040527344, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=0.8901944160461426, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=0.9058809280395508, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=0.9372539520263672, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0,  pitch=1.0, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=-0.14508499205112457, pitch=1.0, yaw=-0.14508499205112457, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=-0.2862636148929596, pitch=1.0, yaw=-0.2862636148929596, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=-0.14508499205112457, pitch=1.0, yaw=-0.14508499205112457, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=-0.19214454293251038, pitch=1.0, yaw=-0.19214454293251038, jump=True, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=-0.23920407891273499, pitch=1.0, yaw=-0.23920407891273499, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=-0.2627338469028473, pitch=1.0, yaw=-0.2627338469028473, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=-0.2705771028995514, pitch=1.0, yaw=-0.2705771028995514, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=-0.2784203588962555, pitch=1.0, yaw=-0.2784203588962555, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=-0.2548905909061432, pitch=1.0, yaw=-0.2548905909061432, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.0, steer=-0.20783105492591858, pitch=0.8274483680725098, yaw=-0.20783105492591858, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.14508499205112457, steer=-0.13724173605442047, pitch=0.5686208605766296, yaw=-0.13724173605442047, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.21959593892097473,  pitch=0.2862636148929596, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.3019501268863678,  pitch=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.3960692286491394,  pitch=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.43920713663101196,  pitch=0.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.4823450446128845,  pitch=-0.12942899763584137, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.5529343485832214,  pitch=-0.23923459649085999, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.6156803965568542,  pitch=-0.3568834364414215, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.6784264445304871,  pitch=-0.4745323061943054, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.8039186000823975,  pitch=-0.6235541701316833, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.8509781360626221,  pitch=-0.7333597540855408, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.9098025560379028, steer=0.20001831650733948, pitch=-0.9137547016143799, yaw=0.20001831650733948, roll=-1.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=0.9568620920181274,  pitch=-1.0, roll=-1.0, jump=False, boost=False, handbrake=False),
ControllerState(throttle=1.0, steer=0.10589922964572906, pitch=-1.0, yaw=0.10589922964572906, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.12942899763584137, pitch=-1.0, yaw=0.12942899763584137, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.12158574163913727, pitch=-1.0, yaw=0.12158574163913727, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.12158574163913727, pitch=-1.0, yaw=0.12158574163913727, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.12158574163913727, pitch=-1.0, yaw=0.12158574163913727, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.11374248564243317, pitch=-1.0, yaw=0.11374248564243317, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.11374248564243317, pitch=-1.0, yaw=0.11374248564243317, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.10589922964572906, pitch=-1.0, yaw=0.10589922964572906, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.2862941324710846, pitch=-1.0, yaw=0.2862941324710846, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.2941373884677887, pitch=-1.0, yaw=0.2941373884677887, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.3019806444644928, pitch=-1.0, yaw=0.3019806444644928, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.23139134049415588, pitch=-1.0, yaw=0.23139134049415588, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.22354808449745178, pitch=-1.0, yaw=0.22354808449745178, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.21570482850074768, pitch=-1.0, yaw=0.21570482850074768, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.2941373884677887, pitch=-1.0, yaw=0.2941373884677887, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.23139134049415588, pitch=-1.0, yaw=0.23139134049415588, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.21570482850074768, pitch=-1.0, yaw=0.21570482850074768, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.12942899763584137, pitch=-1.0, yaw=0.12942899763584137, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0,  pitch=-1.0, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.10589922964572906, pitch=-1.0, yaw=0.10589922964572906, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.11374248564243317, pitch=-1.0, yaw=0.11374248564243317, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.12158574163913727, pitch=-1.0, yaw=0.12158574163913727, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.14511550962924957, pitch=-1.0, yaw=0.14511550962924957, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.16864527761936188, pitch=-1.0, yaw=0.16864527761936188, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.21570482850074768, pitch=-1.0, yaw=0.21570482850074768, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.2549211084842682, pitch=-1.0, yaw=0.2549211084842682, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.2784508764743805, pitch=-1.0, yaw=0.2784508764743805, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.3490401804447174, pitch=-1.0, yaw=0.3490401804447174, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.3960997462272644, pitch=-1.0, yaw=0.3960997462272644, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.443159282207489, pitch=-1.0, yaw=0.443159282207489, roll=-1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.4823755621910095, pitch=-1.0, yaw=0.4823755621910095, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.52159184217453, pitch=-1.0, yaw=0.52159184217453, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.6392406821250916, pitch=-1.0, yaw=0.6392406821250916, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.6078676581382751, pitch=-1.0, yaw=0.6078676581382751, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.6313974261283875, pitch=-1.0, yaw=0.6313974261283875, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.6863002181053162, pitch=-1.0, yaw=0.6863002181053162, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.7255164980888367, pitch=-1.0, yaw=0.7255164980888367, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.7568895816802979, pitch=-0.9765007495880127, yaw=0.7568895816802979, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.8039491176605225, pitch=-0.9451277256011963, yaw=0.8039491176605225, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.8353221416473389, pitch=-0.8980681896209717, yaw=0.8353221416473389, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.8588519096374512, pitch=-0.8666951656341553, yaw=0.8588519096374512, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.8745384216308594, pitch=-0.8353221416473389, yaw=0.8745384216308594, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.8902249336242676, pitch=-0.8117923736572266, yaw=0.8902249336242676, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.9137547016143799, pitch=-0.7804193496704102, yaw=0.9137547016143799, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.9294412136077881, pitch=-0.7568895816802979, yaw=0.9294412136077881, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.9451277256011963, pitch=-0.7333597540855408, yaw=0.9451277256011963, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.9529709815979004, pitch=-0.7176732420921326, yaw=0.9529709815979004, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.9608142375946045, pitch=-0.6941434741020203, yaw=0.9608142375946045, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.9686574935913086, pitch=-0.6784569621086121, yaw=0.9686574935913086, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.9921872615814209, pitch=-0.6549271941184998, yaw=0.9921872615814209, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.9921872615814209, pitch=-0.6313974261283875, yaw=0.9921872615814209, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.9921872615814209, pitch=-0.6078676581382751, yaw=0.9921872615814209, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.5921811461448669, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.5686513781547546, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.5608081221580505, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.5451216101646423, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.5372783541679382, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.52159184217453, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.52159184217453, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.9921872615814209, pitch=-0.5059053301811218, yaw=0.9921872615814209, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=0.9765007495880127, pitch=-0.4902188181877136, yaw=0.9765007495880127, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4745323061943054, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4666890501976013, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4588457942008972, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4510025382041931, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4510025382041931, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.443159282207489, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4353160262107849, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4274727702140808, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4196295142173767, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4117862582206726, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4117862582206726, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4117862582206726, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4117862582206726, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4117862582206726, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4117862582206726, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4117862582206726, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4117862582206726, yaw=1.0, jump=False, boost=True, handbrake=False),
ControllerState(throttle=1.0, steer=1.0, pitch=-0.4117862582206726, yaw=1.0, jump=False, boost=True, handbrake=False),
]

LEFT_DIAG_KICKOFF_FAKE = (
        11 * 4 * [ControllerState(throttle=-1)]
        + helper_fake_left
)

RIGHT_DIAG_KICKOFF_FAKE = (
        11 * 4 * [ControllerState(throttle=-1)]
        + helper_fake_right
)


RIGHT_MID_KICKOFF_SPEEDFLIP = (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 6 * 4 * [ControllerState(throttle=1, boost=True, steer=-1)]
        + 2 * 4 * [ControllerState(throttle=1, boost=True, steer=1)]
        + 2 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=0.8, pitch=-0.7, jump=True, boost=True)]
        + 13 * 4 * [ControllerState(throttle=1, roll=0.5, pitch=1, boost=True, handbrake=True)]
        + 12 * 4 * [ControllerState(throttle=1, roll=1, pitch=0.5, handbrake=True)]
)

RIGHT_MID_KICKOFF_FAKE= (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 6 * 4 * [ControllerState(throttle=1, boost=True, steer=-1)]
        + 2 * 4 * [ControllerState(throttle=1, boost=True, steer=1)]
        + 2 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=0.8, pitch=-0.7, jump=True, boost=True)]
        + 13 * 4 * [ControllerState(throttle=1, roll=0.5, pitch=1, boost=True, handbrake=True)]
        + 12 * 4 * [ControllerState(throttle=1, roll=1, pitch=0.5, handbrake=True)] 
        + 20 * 4 * [ControllerState(throttle=1, steer=-1)]
)

RIGHT_MID_KICKOFF_FAKE_SPANISH= (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 6 * 4 * [ControllerState(throttle=1, boost=True, steer=-1)]
        + 2 * 4 * [ControllerState(throttle=1, boost=True, steer=1)]
        + 2 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=0.8, pitch=-0.7, jump=True, boost=True)]
        + 13 * 4 * [ControllerState(throttle=1, roll=0.5, pitch=1, boost=True, handbrake=True)]
        + 12 * 4 * [ControllerState(throttle=1, roll=1, pitch=0.5, handbrake=True)] 
        + 17 * 4 * [ControllerState(throttle=1, steer=-1)]
)


RIGHT_MID_KICKOFF_FAKE_CHEATER= (
        25 * 4 * [ControllerState(throttle=-1)]
        + 33 * 4 * [ControllerState()]
        + 10 * 4 * [ControllerState(throttle=1)]
)



RIGHT_MID_SIMPLE_DELAYED = (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 6 * 4 * [ControllerState(throttle=1, boost=True, steer=-1)]
        + 2 * 4 * [ControllerState(throttle=1, boost=True, steer=1)]
        + 2 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=False)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=0.8, pitch=-0.9, jump=True, boost=False)]
        + 13 * 4 * [ControllerState(throttle=1, roll=0.5, pitch=1, boost=False, handbrake=True)]
        + 12 * 4 * [ControllerState(throttle=1, roll=1, pitch=0.5, handbrake=True)]
)


LEFT_MID_KICKOFF_SPEEDFLIP = (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 6 * 4 * [ControllerState(throttle=1, boost=True, steer=1)]
        + 2 * 4 * [ControllerState(throttle=1, boost=True, steer=-1)]
        + 2 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=-0.8, pitch=-0.7, jump=True, boost=True)]
        + 13 * 4 * [ControllerState(throttle=1, roll=-0.5, pitch=1, boost=True, handbrake=True)]
        + 10 * 4 * [ControllerState(throttle=1, roll=-1, pitch=0.5, handbrake=True)]
)

LEFT_MID_KICKOFF_FAKE = (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 6 * 4 * [ControllerState(throttle=1, boost=True, steer=1)]
        + 2 * 4 * [ControllerState(throttle=1, boost=True, steer=-1)]
        + 2 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=-0.8, pitch=-0.7, jump=True, boost=True)]
        + 13 * 4 * [ControllerState(throttle=1, roll=-0.5, pitch=1, boost=True, handbrake=True)]
        + 10 * 4 * [ControllerState(throttle=1, roll=-1, pitch=0.5, handbrake=True)]
        + 20 * 4 * [ControllerState(throttle=1, steer=1)]
)

LEFT_MID_KICKOFF_FAKE_SPANISH = (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 6 * 4 * [ControllerState(throttle=1, boost=True, steer=1)]
        + 2 * 4 * [ControllerState(throttle=1, boost=True, steer=-1)]
        + 2 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=-0.8, pitch=-0.7, jump=True, boost=True)]
        + 13 * 4 * [ControllerState(throttle=1, roll=-0.5, pitch=1, boost=True, handbrake=True)]
        + 10 * 4 * [ControllerState(throttle=1, roll=-1, pitch=0.5, handbrake=True)]
        + 17 * 4 * [ControllerState(throttle=1, steer=1)]
)


LEFT_MID_KICKOFF_FAKE_CHEATER = (
        25 * 4 * [ControllerState(throttle=-1)]
        + 31 * 4 * [ControllerState()]
        + 10 * 4 * [ControllerState(throttle=1)]
)


LEFT_MID_SIMPLE_DELAYED = (
        11 * 4 * [ControllerState(throttle=1, boost=True)]
        + 6 * 4 * [ControllerState(throttle=1, boost=True, steer=1)]
        + 2 * 4 * [ControllerState(throttle=1, boost=True, steer=-1)]
        + 2 * 4 * [ControllerState(throttle=1, jump=True, boost=True)]
        + 1 * 4 * [ControllerState(throttle=1, boost=False)]
        + 1 * 4 * [ControllerState(throttle=1, yaw=-0.8, pitch=-0.9, jump=True, boost=False)]
        + 13 * 4 * [ControllerState(throttle=1, roll=-0.5, pitch=1, boost=False, handbrake=True)]
        + 10 * 4 * [ControllerState(throttle=1, roll=-1, pitch=0.5, handbrake=True)]
)
