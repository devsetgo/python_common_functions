from loguru import logger
from pathlib import Path


def config_logging():
    log_path = Path.cwd().joinpath("log").joinpath("app_log.log")
    logger.add(
        log_path,
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
        rotation="10 MB",
        retention="10 days",
        enqueue=True,
        backtrace=False,
        # compresson="zip",
    )
