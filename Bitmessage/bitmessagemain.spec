# -*- mode: python -*-
a = Analysis(['C:\\Users\\David\\Desktop\\BlackHalo\\Halo\\BitMessage\\bitmessagemain.py'],
             pathex=['C:\\Users\\David\\Desktop\\BlackHalo\\Halo\\BitMessage'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='bitmessagemain.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='BitMHalo.ico')
