import json
import csv
import os
from pathlib import Path
from datetime import datetime, timedelta
import time
import random

# remove loguru and place your favorite logging mechanism
from loguru import logger


log_path = Path.cwd().joinpath("log").joinpath("app_log.log")
logger.add(log_path, rotation="1 MB", enqueue=True, backtrace=True)

# Directory Path
directory_to__files = "data"


# get list of files in directory
def get_data_directory_list(directory: str):
    file_directory = f"{directory_to__files}/{directory}"
    directory_path = Path.cwd().joinpath(file_directory)
    # iterate through directory
    try:
        file_list = os.listdir(directory_path)
        return file_list
    except Exception as e:
        # log error if
        logger.critical(e)
        # return status
        data = {"error": f"{e}"}
        return data


# Json File Processing
# Json Save new file
def save_json(filename: str, data: dict):
    # add extension to file name
    file_name = f"{filename}"
    file_directory = f"{directory_to__files}/json"
    # create file in filepath
    file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)
    try:

        # open/create file
        with open(file_save, "w+") as write_file:
            # write data to file
            json.dump(data, write_file)

        logger.info(f"File Create: {file_name}")
        return "complete"
    except FileNotFoundError as e:
        # log error if
        logger.critical(e)
        # return status
        data = {"error": f"ERROR: no file named {filename} in location {file_save}"}
        return data


# TODO: figure out a method of appending an existing json file
# def append_json(filename, data):
#     return 'some result'

# Json Open file
def open_json(filename: str):
    # add extension to file name
    file_name = f"{filename}"
    file_directory = f"{directory_to__files}/json"
    # create file in filepath
    file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)
    # Try/Except block
    try:
        # open file
        with open(file_save) as read_file:
            # load file into data variable
            data = json.load(read_file)

        logger.info(f"File Opened: {file_name}")
        return data

    except FileNotFoundError as e:
        # log error if
        logger.critical(e)
        # return status
        data = {"error": f"ERROR: no file named {file_name} in location {file_save}"}
        return data


# CSV File Processing
# CSV Save new file
def save_csv(filename: str, data: list):
    # add extension to file name
    file_name = f"{filename}"
    file_directory = f"{directory_to__files}/csv"
    # create file in filepath
    file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)

    try:
        # open/create file
        with open(file_save, "w+", encoding="utf-8", newline="") as write_file:
            # write data to file
            file_writer = csv.writer(
                write_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            for row in data:
                file_writer.writerow(row)

        logger.info(f"File Create: {file_name}")
        return "complete"
    except FileNotFoundError as e:
        # log error if
        logger.critical(e)
        # return status
        data = {"error": f"ERROR: no file named {filename} in location {file_save}"}
        return data


# TODO: figure out a method of appending an existing json file
# def append_json(filename, data):
#     return 'some result'

# TODO: Figure out a method of appending existing CSV files
# def append_csv(filename, data):
#     return 'some result'


# CSV Open file
# pass file name and optional delimiter (default is ',')
# Output is dictionary/json
# expectation is for file to be quote minimal and skipping initial spaces is a good thing
# modify as needed
def open_csv(filename: str, delimit: str = None):
    if delimit == None:
        delimit = ","
    # add extension to file name
    file_name = f"{filename}"
    file_directory = f"{directory_to__files}/csv"
    # create file in filepath
    file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)
    # Try/Except block
    try:
        # open file
        data = []
        with open(file_save) as read_file:
            # load file into data variable
            csv_data = csv.DictReader(
                read_file,
                delimiter=delimit,
                quoting=csv.QUOTE_MINIMAL,
                skipinitialspace=True,
            )

            # convert list to JSON object
            title = csv_data.fieldnames
            # iterate through each row to create dictionary/json object
            for row in csv_data:
                data.extend([{title[i]: row[title[i]] for i in range(len(title))}])
            logger.info(f"File Opened: {file_name}")
        return data
    except FileNotFoundError as e:
        # log error if
        logger.critical(e)
        # return status
        data = {"error": f"ERROR: no file named {file_name} in location {file_save}"}
        return data


def create_sample_files(filename: str, sample_size: int):

    first_name = [
        "Daniel",
        "Catherine",
        "Valerie",
        "Mike",
        "Kristina",
        "Linda",
        "Olive",
        "Mollie",
        "Nadia",
        "Elisha",
        "Lorraine",
        "Nedra",
        "Voncile",
        "Katrina",
        "Alan",
        "Clementine",
        "Kanesha",
    ]

    csv_data = []
    count = 0
    for i in range(sample_size):
        r_int = random.randint(0, len(first_name) - 1)
        if count == 0:
            sample_dict = ["name", "birth_date"]
        else:
            sample_dict = [first_name[r_int], str(gen_datetime())]
        count += 1
        csv_data.append(sample_dict)

    csv_file = f"{filename}.csv"
    result = save_csv(csv_file, csv_data)

    json_data = []
    for i in range(sample_size):
        r_int = random.randint(0, len(first_name) - 1)
        sample_dict = {"name": first_name[r_int], "birthday_date": str(gen_datetime())}
        json_data.append(sample_dict)
    json_file = f"{filename}.json"
    result = save_json(json_file, json_data)


def gen_datetime(min_year: int = None, max_year: int = None):
    if min_year is None:
        min_year = 1900
    if max_year is None:
        max_year = datetime.now().year
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    year = random.randint(min_year, max_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 12)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    date_value = datetime(year, month, day, hour, minute, second)

    # print(date_value)
    return date_value


# if __name__ == '__main__':
#     # create_sample_files('test_x',2)
#     create_sample_files()
