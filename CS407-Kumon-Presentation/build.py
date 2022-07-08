#!/usr/bin/env python

from pathlib import Path
import subprocess
import PyInstaller.__main__

root_dir = Path(__file__).parent
subprocess.call('npm install', cwd=root_dir / 'frontend', shell=True)
subprocess.call('npm run build', cwd=root_dir / 'frontend', shell=True)
subprocess.call('python manage.py collectstatic --noinput', cwd=root_dir, shell=True)
PyInstaller.__main__.run([
    str(root_dir / 'gui.spec'),
    '--noconfirm',
    '--distpath',
    str(root_dir / 'dist'),
    '--workpath',
    str(root_dir / 'build'),
])
