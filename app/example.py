""" An example of functions in the common library"""
import time
from datetime import datetime
from pathlib import Path
from com_lib.file_functions import (
    open_json,
    open_csv,
    create_sample_files,
    get_data_directory_list,
)
from com_lib.folder_functions import (
    get_directory_list,
    last_data_files_changed,
    make_folder,
)

from com_lib.logging_config import config_logging

# remove loguru and place your favorite logging mechanism
from loguru import logger

config_logging()


def call_folder_functions():
    dir_list_func()
    dir_create()
    last_change()
    make_dir()


def dir_list_func():
    dir_list = get_directory_list("data")
    print(dir_list)
    for i in dir_list:
        x = str(i)
        if "csv" in x:
            p = i
            name = "data/cs_v"
            x = p.rename(name)

    # Pause so you can see the change
    time.sleep(5)

    dir_list = get_directory_list("data")
    print(dir_list)
    for i in dir_list:
        x = str(i)
        if "cs_v" in x:
            p = i
            name = "data/csv"
            x = p.rename(name)


def dir_create():
    d = datetime.now().strftime("%Y-%H-%M-%S")
    print(d)
    directory_to__files: str = "data"
    file_directory = f"{directory_to__files}/{d}"
    directory_path = Path.cwd().joinpath(file_directory)


def last_change():
    directory_to__files: str = "data"
    file_directory = f"{directory_to__files}"
    directory_path = Path.cwd().joinpath(file_directory)
    last_data_files_changed(directory_path)


def make_dir():
    d = datetime.now().strftime("%Y-%H-%M-%S")
    print(d)
    directory_to__files: str = "data"
    file_directory = f"{directory_to__files}/{d}"
    directory_path = Path.cwd().joinpath(file_directory)

    for i in range(2):
        make_folder(directory_path)


def get_data():
    filename: str = "test_1.json"
    try:
        result: dict = open_json(filename)
    except Exception as e:
        print(e)


def make_sample():
    filename: str = "sample"
    sample_size: int = 1000
    try:
        result = create_sample_files(filename, sample_size)
    except Exception as e:
        print(e)


def dir_list():
    directory: str = "json"
    try:
        directory_list: list = get_data_directory_list(directory)
    except Exception as e:
        print(e)

    try:
        for i in directory_list:
            result: dict = open_json(i)
            count = 0
            for n in result:
                x = n["name"]
                count += 1
            print(count)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_data()
    make_sample()
    dir_list()
    call_folder_functions()
