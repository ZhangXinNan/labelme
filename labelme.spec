# -*- mode: python -*-
# vim: ft=python

<<<<<<< HEAD

block_cipher = None


a = Analysis(
    ['labelme/main.py'],
=======
import sys


sys.setrecursionlimit(5000)  # required on Windows


a = Analysis(
    ['labelme/__main__.py'],
>>>>>>> upstream/master
    pathex=['labelme'],
    binaries=[],
    datas=[
        ('labelme/config/default_config.yaml', 'labelme/config'),
        ('labelme/icons/*', 'labelme/icons'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
<<<<<<< HEAD
    excludes=['matplotlib'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
=======
    excludes=[],
)
pyz = PYZ(a.pure, a.zipped_data)
>>>>>>> upstream/master
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='labelme',
    debug=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,
    icon='labelme/icons/icon.ico',
)
app = BUNDLE(
    exe,
<<<<<<< HEAD
    name='labelme.app',
=======
    name='Labelme.app',
>>>>>>> upstream/master
    icon='labelme/icons/icon.icns',
    bundle_identifier=None,
    info_plist={'NSHighResolutionCapable': 'True'},
)
