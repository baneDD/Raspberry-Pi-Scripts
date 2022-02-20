import RPi.GPIO as GPIO
from time import sleep
import logging

logger = logging.getLogger('network_monitor.router')


def perform_reset():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    logger.info("Powering down the router!")

    GPIO.output(22, True)
    GPIO.output(23, True)

    sleep(30)

    logger.info("Bringing router back up!")

    GPIO.output(22, False)
    GPIO.output(23, False)

    GPIO.cleanup()
