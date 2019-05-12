import json
import csv
from pathlib import Path
import datetime
import time
# remove loguru and place your favorite logging mechanism
from loguru import logger


log_path = Path.cwd().joinpath("log").joinpath("app_log.log")
logger.add(log_path, rotation="500 MB", enqueue=True, backtrace=True)

# Directory Path
directory_to__files = "fileproc/data"

# Json File Processing
# Json Save new file
def save_json(filename, data):
    try:
        # add extension to file name
        file_name = f"{filename}.json"
        file_directory = f"{directory_to__files}/json"
        # create file in filepath
        file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)
        # open/create file
        with open(file_save, "w+") as write_file:
            # write data to file
            json.dump(data, write_file)

        logger.info(f"File Create: {file_name}")
        return "complete"
    except Exception as e:
        # log error if
        logger.critical(e)
        # return status
        data = {"error": f"ERROR: no file named {filename} in location {file_save}"}
        return data


# TODO: figure out a method of appending an existing json file
# def append_json(filename, data):
#     return 'some result'

# Json Open file
def open_json(filename):
    # Try/Except block
    try:
        # add extension to file name
        file_name = f"{filename}.json"
        file_directory = f"{directory_to__files}/json"
        # create file in filepath
        file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)
        # open file
        with open(file_save) as read_file:
            # load file into data variable
            data = json.load(read_file)
        
        logger.info(f"File Opened: {file_name}")
        return data

    except Exception as e:
        # log error if
        logger.critical(e)
        # return status
        data = {
            "error": f"ERROR: no file named {file_name} in location {file_save}"
        }
        return data


# CSV File Processing
# CSV Save new file
def save_csv(filename, data):
    try:
        # add extension to file name
        file_name = f"{filename}.csv"
        file_directory = f"{directory_to__files}/csv"
        # create file in filepath
        file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)
        # open/create file
        with open(file_save, "w+", encoding='utf-8',newline="") as write_file:
            # write data to file
            file_writer = csv.writer(
                write_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in data:
                file_writer.writerow(row)
        
        logger.info(f"File Create: {file_name}")
        return "complete"
    except Exception as e:
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
# expectation is for file to be quote minimal and skippng inistial spaces is a good thing
# modify as needed
def open_csv(filename, delimit=None):
    if delimit == None:
        delimit = ","
    # Try/Except block
    try:
        # add extension to file name
        file_name = f"{filename}.csv"
        file_directory = f"{directory_to__files}/csv"
        # create file in filepath
        file_save = Path.cwd().joinpath(file_directory).joinpath(file_name)
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

    except Exception as e:
        # log error if
        logger.critical(e)
        # return status
        data = {
            "error": f"ERROR: no file named {file_name} in location {file_save}"
        }
        return data


