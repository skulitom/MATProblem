import logging
import os
import sys


def start_logger():

    # main
    init_logger('main')

    # parser
    init_logger('parser')

    # visualization
    init_logger('visual')

    # algorithm
    init_logger('robot')

    # graph
    init_logger('graph')


def init_logger(name):

    if name is None:
        raise ValueError

    print("[*] Initiating %s Logger" % name)

    # Log format
    log_format = logging.Formatter("%(asctime)s [%(levelname)s] - [*] %(message)s")

    # Create logger
    logger = logging.getLogger(name + '_logger')
    logger.setLevel(logging.INFO)

    file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    if not os.path.exists('%s/log' % file_path):
        print('Creating log directroy %s/log' % file_path)
        os.makedirs('%s/log' % file_path)

    if not os.path.exists('%s/log/%s' % (file_path, name)):
        print('Creating directory %s/log/%s' % (file_path, name))
        os.makedirs('%s/log/%s' % (file_path, name))

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
    stream_handler.setLevel(logging.DEBUG)

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