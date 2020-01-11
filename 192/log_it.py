import logging
from typing import Callable
# print(callable(logging.info))
DEBUG = logging.debug
INFO = logging.info
WARNING = logging.warning
ERROR = logging.error
CRITICAL = logging.critical


def log_it(level: Callable, msg: str) -> None:
    level_name = level.__name__
    logger = logging.getLogger("pybites_logger")
    if level_name == "debug":
        logger.log(level=10, msg=msg)
    elif level_name == "info":
        logger.log(level=20, msg=msg)
    elif level_name == "warning":
        logger.log(level=30, msg=msg)
    elif level_name == "error":
        logger.log(level=40, msg=msg)
    elif level_name == "critical":
        logger.log(level=50, msg=msg)



if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")