import logging
from typing import Callable

pybites_logger = logging.getLogger("pybites_logger")
DEBUG = pybites_logger.debug
INFO = pybites_logger.info
WARNING = pybites_logger.warning
ERROR = pybites_logger.error
CRITICAL = pybites_logger.critical


def log_it(level: Callable, msg: str) -> None:
    level(msg)
    # level_name = level.__name__
    # logger = logging.getLogger("pybites_logger")
    # if level_name == "debug":
    #     logger.log(level=10, msg=msg)
    # elif level_name == "info":
    #     logger.log(level=20, msg=msg)
    # elif level_name == "warning":
    #     logger.log(level=30, msg=msg)
    # elif level_name == "error":
    #     logger.log(level=40, msg=msg)
    # elif level_name == "critical":
    #     logger.log(level=50, msg=msg)

# print(log_it.__annotations__)

if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")