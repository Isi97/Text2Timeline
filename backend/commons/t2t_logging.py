import logging
from re import T





def log_info(message: str):
    logging.info(message)


def initialize_logging() -> None:
    logging_initialized = True
    level = logging.INFO
    # attributes from the LogRecord class
    _format = "[%(levelname)s] %(filename)s %(asctime)s - %(message)s"
    logging.basicConfig(level=level, format=_format)