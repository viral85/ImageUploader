import logging
import os
from logging.handlers import TimedRotatingFileHandler


class LogConfiguration:
    logger_name: str = "file-upload"
    logger_formatter: str = "%(asctime)s-%(levelname)s-%(name)s-%(process)d-%(pathname)s|%(lineno)s:: %(funcName)s|%(" \
                            "lineno)s:: %(message)s "
    roll_over: str = "MIDNIGHT"
    backup_count: int = 90
    log_file_base_name: str = "log"
    log_file_base_dir: str = f"{os.getcwd()}/logs"


def get_logger():
    """
    Logging Configurations.
    """
    logger = logging.getLogger(LogConfiguration.logger_name)
    formatter = logging.Formatter(LogConfiguration.logger_formatter)
    handler = TimedRotatingFileHandler(
        filename=os.path.join(LogConfiguration.log_file_base_dir, LogConfiguration.log_file_base_name),
        when=LogConfiguration.roll_over, interval=1, backupCount=LogConfiguration.backup_count)
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


app_logger = get_logger()
