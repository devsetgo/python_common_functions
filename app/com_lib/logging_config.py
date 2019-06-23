from loguru import logger
from pathlib import Path

def config_logging():
    log_path = Path.cwd().joinpath("log").joinpath("app_log.log")
    logger.add(
        log_path,
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
        enqueue=True,
        backtrace=False,
        rotation="100 MB",
        retention="30 days",
        # compression="zip",
        # serialize=True,
        )
