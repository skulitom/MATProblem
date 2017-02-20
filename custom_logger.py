import logging
import os
import sys


def start_logger():

    # main
    init_logger('main')


def init_logger(name):

    if name is None:
        raise ValueError

    print("[*] Initiating %s Logger" % name)

    # Log format
    log_format = logging.Formatter("%(asctime)s [%(levelname)s] - [*] %(message)s")

    # Create logger
    logger = logging.getLogger(name + '_logger')
    logger.setLevel(logging.INFO)

    # file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_path = os.path.dirname(os.path.realpath(__file__))

    # Create handler
    # Info-level log
    info_handler = logging.FileHandler(filename='%s/log/%s/%s_info.log' % (file_path, name, name))
    info_handler.setLevel(logging.INFO)
    info_handler.addFilter(LevelFilter(logging.INFO))

    # Critical-level log
    critical_handler = logging.FileHandler(filename='%s/log/%s/%s_critical.log' % (file_path, name, name))
    critical_handler.setLevel(logging.CRITICAL)

    # Stream log
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)

    # Set formats to handlers
    info_handler.setFormatter(log_format)
    critical_handler.setFormatter(log_format)
    stream_handler.setFormatter(log_format)

    # Add handlers to logger
    logger.addHandler(info_handler)
    logger.addHandler(critical_handler)
    logger.addHandler(stream_handler)

    print("[*] Initiated %s Logger\n" % name)


# Filter to log only the level
class LevelFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level