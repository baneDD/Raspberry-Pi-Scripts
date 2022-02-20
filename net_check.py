import os
import threading
import urllib.request
import re
import logging
import router

from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('network_monitor')
logger.setLevel(logging.INFO)


def main():
    setup_logging('network_monitor.log')


def setup_logging(path):
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fileHandler = TimedRotatingFileHandler(path,
                                           when="h",
                                           interval=24,
                                           backupCount=30)
    fileHandler.setFormatter(formatter)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    logger.info('Logging set up complete')


def get_external_ip():
    url = 'http://checkip.dyndns.org'
    request = urllib.request.urlopen(url).read().decode('utf-8')
    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', request)

    return ip


def check_ping():
    hostname = 'google.com'
    response = os.system('ping -c 1 ' + hostname + ' > /dev/null 2>&1')

    return response


if __name__ == '__main__':
    main()
