# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/gui_wx.py'],
    pathex=['src'],
    binaries=[],
    datas=[('src/help.htm', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LaSolv',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='arm64',
    codesign_identity=None,
    entitlements_file=None,
    icon=['src/LaSolv_icon.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='LaSolv',
)
app = BUNDLE(
    coll,
    name='LaSolv.app',
    icon='src/LaSolv_icon.icns',
    bundle_identifier=None,
)
