# -*- mode: python -*-



block_cipher = None





a = Analysis(['bitbay/BitMHalo.py'],

             pathex=['src', '/home/admin0/Halo/Bitmessage-BitMHalo-v0.6'],

             binaries=[],

             datas=[('bitmsghash.so', 'bitmsghash')],

             hiddenimports=[],

             hookspath=[],

             runtime_hooks=[],

             excludes=[],

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

          console=True , uac_admin=True, icon='bitbay/BitMHalo.ico')