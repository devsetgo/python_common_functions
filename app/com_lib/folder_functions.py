import json
import csv
import os
from typing import (
    List,
    Dict,
    Tuple,
    Sequence,
    Mapping,
    Iterable,
    TypeVar,
    Generic,
    Sized,
    Union,
    Any,
    Optional,
)
from pathlib import Path
from datetime import datetime, timedelta
import time
import random
from com_lib.logging_config import config_logging

# remove loguru and place your favorite logging mechanism
from loguru import logger

config_logging()

# Directory Path
directory_to__files: str = "data"
file_directory = f"{directory_to__files}\csv"  # /{directory}"
directory_path = Path.cwd().joinpath(file_directory)

# get list of files in directory
# def get_data_directory_list(directory: str):
#     file_directory = f"{directory_to__files}/{directory}"
#     directory_path = Path.cwd().joinpath(file_directory)
#     # iterate through directory
#     try:
#         file_list: list = os.listdir(directory_path)
#         return file_list
#     except Exception as e:
#         # log error if
#         logger.error(e)
#         # return status
#         error: dict = {"error": f"{e}"}
#         return error

# def tree(directory):
#     print(f'+ {directory}')
#     for path in sorted(directory.rglob('*')):
#         depth = len(path.relative_to(directory).parts)
#         spacer = '    ' * depth
#         print(f'{spacer}+ {path.name}')


def last_data_files_changed(directory_path):
    print(directory_path)
    time, file_path = max((f.stat().st_mtime, f) for f in directory_path.iterdir())
    # print(datetime.fromtimestamp(time), file_path)
    return time, file_path


def get_directory_list(file_directory):
    """ getting a list of directories"""
    direct_list = []
    file_path = Path.cwd().joinpath(file_directory)
    for x in file_path.iterdir():
        if x.is_dir():
            direct_list.append(x)

    return direct_list


def make_folder(file_directory):
    """ making a folder in a specific directory"""
    try:
        os.makedirs(file_directory)
        logger.info(f"direct created: hi")
    except Exception as e:
        # log error if
        logger.error(e)
        error: dict = {"error": f"{e}"}
        return error


# if __name__ == '__main__':
#     one()
