import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(
#             filename=".\\Logs\\automation.log",
#             format='%(asctime)s: %(levelname)s: %(message)s',
#             datefmt='%m/%d/%y %I:%M:%S %p'
#         )
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger

import sys
from logging.handlers import TimedRotatingFileHandler
FORMATTER= logging.Formatter("%(asctime)s:%(levelname)s: %(message)s")
LOG_FILE=".\\LOGS\\my_app.log"

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE,when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger(logger_name):
    logger=logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate=False
    return logger