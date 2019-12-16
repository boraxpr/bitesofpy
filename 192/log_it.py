import logging
from typing import Callable

DEBUG = "..."
INFO = "..."
WARNING = "..."
ERROR = "..."
CRITICAL = "..."


def log_it(level: Callable, msg: str) -> None:
    logging.Call


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")