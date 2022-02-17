import os
import threading
import urllib.request
import re
import logging


logging.basicConfig(filename='network_monitor.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


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


def check_ping_timer():
    threading.Timer(5.0, check_ping_timer).start()
    res = check_ping()
    logging.debug(res)


ext_ip = get_external_ip()
if len(ext_ip):
    logging.debug("External IP is " + ext_ip[0])
check_ping_timer()
