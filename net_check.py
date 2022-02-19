import os
import threading
import urllib.request
import re
import logging
import router


from logging.handlers import TimedRotatingFileHandler


def main():
    create_timed_rotating_log("netmon.log")
    router.perform_reset()


def create_timed_rotating_log(path):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(path,
                                       when="d",
                                       interval=1,
                                       backupCount=30)
    logger.addHandler(handler)


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
