# -*- mode: python -*-

block_cipher = None


a = Analysis(['frontend.py'],
<<<<<<< HEAD
             pathex=['/Users/nguyeant/Documents/GitHub/Python10Apps/App5'],
=======
             pathex=['C:\\Users\\nguyeant\\Downloads\\Python\\10Apps\\Python10Apps\\App5'],
>>>>>>> e2d258aa48b9b565039316e7c6f71f86a3ba4a22
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='frontend',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
<<<<<<< HEAD
app = BUNDLE(exe,
             name='frontend.app',
             icon=None,
             bundle_identifier=None)
=======
>>>>>>> e2d258aa48b9b565039316e7c6f71f86a3ba4a22
