# -*- coding: utf-8 -*-
""" Starting point of the application """

"""
Load configuration settings
"""
from settings import APP_VERSION
from settings import HOST_DOMAIN
from settings import LICENSE_LINK
from settings import LICENSE_TYPE
from settings import LOGURU_BACKTRACE
from settings import LOGURU_RETENTION
from settings import LOGURU_ROTATION
from settings import OWNER
from settings import RELEASE_ENV
from settings import SECRET_KEY
from settings import SQLALCHEMY_DATABASE_URI
from settings import WEBSITE

"""
Init logging
"""
# config_logging()
# logger.info("API Logging inititated")


def main():
    thing = [
        APP_VERSION,
        OWNER,
        WEBSITE,
        LICENSE_TYPE,
        LICENSE_LINK,
        HOST_DOMAIN,
        RELEASE_ENV,
        SQLALCHEMY_DATABASE_URI,
        SECRET_KEY,
        LOGURU_BACKTRACE,
        LOGURU_RETENTION,
        LOGURU_ROTATION,
    ]
    for t in thing:
        print(t)


if __name__ == "__main__":
    main()
