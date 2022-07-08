# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'kumon.settings'

imports = [
    'backend_api',
    'frontend_app',
    'whitenoise.middleware',
    'whitenoise.runserver_nostatic',
    'whitenoise.storage',
]

datas = [
    *collect_data_files('coreschema'),
    ('frontend_app/templates', 'frontend_app/templates'),
    ('staticfiles', 'staticfiles'),
]

block_cipher = None

a = Analysis(['gui.py'],
             pathex=[],
             binaries=[],
             datas=datas,
             hiddenimports=imports,
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# Exclude development only files
a.datas = a.datas - TOC([('db.sqlite3', None, None)])
a.datas = TOC([x for x in a.datas if os.path.join('backend_api', 'migrations') not in x[0]])
a.pure = TOC([x for x in a.pure if 'backend_api.migrations' not in x[0]])
a.pure = a.pure - TOC([('kumon.dev_settings', None, None)])
a.pure = TOC([x for x in a.pure if 'backend_api.data_gen' not in x[0]])
a.pure = TOC([x for x in a.pure if not ('backend_api' in x[0] and 'test' in x[0])])

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='kms',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='icon.ico')

app = BUNDLE(exe,
    name='Kumon Management System.app',
    icon='icon.ico')

