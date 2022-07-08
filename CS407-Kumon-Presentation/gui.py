#!/usr/bin/env python
import logging
from logging.handlers import TimedRotatingFileHandler
import subprocess
import multiprocessing
from isort import file
import waitress
from socketserver import TCPServer
import eel
import re

from django.conf import settings
from kumon.wsgi import application

CHROME_PATH = eel.chrome.find_path()
CHROME_PROFILE_PATH = settings.APP_DATA_DIR / 'chrome_profile'
LOG_PATH = settings.APP_DATA_DIR / 'logs'

LOG_FORMAT = '[%(asctime)s] - [%(processName)s] - [%(levelname)s] - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

def serve_django(host, port):
    waitress.serve(application, host=host, port=port)

def log_chrome_output(chrome):
    prev_name = multiprocessing.current_process().name
    multiprocessing.current_process().name = 'CHROME'
    for l in chrome.stdout:
        level = getattr(logging, l.split(':')[3], logging.INFO)
        message = re.sub('\[.*\] ', '', l.rstrip())
        logging.log(level, message)
    multiprocessing.current_process().name = prev_name
    

def main():
    multiprocessing.freeze_support()
    multiprocessing.current_process().name = 'MAIN'
    settings.APP_DATA_DIR.mkdir(parents=True, exist_ok=True)

    LOG_PATH.mkdir(parents=True, exist_ok=True)
    file_handler = TimedRotatingFileHandler(LOG_PATH / 'kms.log', when='midnight', backupCount=7)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))
    logging.getLogger().addHandler(file_handler)

    logging.info('App data directory: %s', settings.APP_DATA_DIR)

    with TCPServer(('localhost', 0), None) as s:
        host, port = s.server_address

    logging.info('Starting django daemon')
    multiprocessing.Process(target=serve_django, args=(host, port), daemon=True, name='DJANGO').start()
    
    if CHROME_PATH is None:
        logging.error("Could not locate chrome installation, exiting")
        return
    
    CHROME_PROFILE_PATH.mkdir(parents=True, exist_ok=True)
    logging.info('Launching chrome with profile %s', CHROME_PROFILE_PATH)
    options = [
        CHROME_PATH,
        f'--app=http://{host}:{port}',
        f"--user-data-dir={CHROME_PROFILE_PATH}",
        '--new-window',
        '--start-maximized',
        '--no-first-run',
    ]
    with subprocess.Popen(options, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, text=True, bufsize=1) as chrome:
        log_chrome_output(chrome)

    logging.info('Chrome closed, exiting')
    

    


if __name__ == '__main__':
    main()
    
