import os
import threading
import urllib.request
import re
import logging
import router

from logging.handlers import TimedRotatingFileHandler
from logging.handlers import StreamHandler


def main():
    setup_logging("netmon.log")
    router.perform_reset()


def setup_logging(path):
    logger = logging.getLogger(__name__)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fileHandler = TimedRotatingFileHandler(path,
                                           when="d",
                                           interval=1,
                                           backupCount=30)
    fileHandler.setLevel(logging.INFO)
    fileHandler.setFormatter(formatter)

    consoleHandler = StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    logger.info("Logging set up complete")


def get_external_ip():
    url = "http://checkip.dyndns.org"
    request = urllib.request.urlopen(url).read().decode('utf-8')
    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', request)
    return ip


def check_ping():
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1")
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus


main()
