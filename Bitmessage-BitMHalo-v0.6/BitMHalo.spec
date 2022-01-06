# -*- mode: python -*-

block_cipher = None


a = Analysis(['bitbay\\BitMHalo.py'],
             pathex=['src', 'C:\\BitBay\\bitbay-pybitmessage-bitbay-v0.6-based'],
             binaries=[],
             datas=[('src/bitmsghash/bitmsghash32.dll', 'bitmsghash')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='BitMHalo',
          debug=False,
          strip=False,
          upx=True,
          console=True , uac_admin=True, icon='bitbay\\BitMHalo.ico')
