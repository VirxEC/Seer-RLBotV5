# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['LeBot/kickoffs.py'],
    pathex=['LeBot'],
    binaries=[],
    datas=[('LeBot/11100.p', '.'), ('LeBot/36000.p', '.'), ('LeBot/43200.p', '.')],
    hiddenimports=['timeit', 'pickletools', 'uuid', 'unittest.mock', 'ctypes.wintypes'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['torch'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='LeBot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
