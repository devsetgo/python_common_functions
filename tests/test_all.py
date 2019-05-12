import json
import csv
import datetime
import time
from fileproc.file_processing import open_json, open_csv, save_json, save_csv


def test_save_json():
    sample_dict = {"name": "bob", "date": str(datetime.datetime.now())}
    file_named = "test_1"
    json_data = []
    for i in range(1000):
        sample_dict = {"name": "bob", "date": str(datetime.datetime.now())}
        json_data.append(sample_dict)

    result = save_json(file_named, json_data)
    assert result == "complete"


def test_save_csv():
    csv_data = []
    file_named = "test_1"
    csv_data = []
    count = 0
    for i in range(1000):
        if count == 0:
            sample_dict = ["name", "date"]
        else:
            sample_dict = ["bob", str(datetime.datetime.now())]
        count += 1
        csv_data.append(sample_dict)

        result = save_csv(file_named, csv_data)
        assert result == "complete"


def test_open_json():
    file_named = "test_1"
    result = open_json(file_named)
    assert len(result) > 1


def test_open_json_no_file():
    file_named = "no_file_name"
    result = open_json(file_named)
    assert result["error"].startswith("ERROR")


def test_open_csv():
    file_named = "test_1"
    result = open_csv(file_named)
    assert len(result) > 1


def test_open_json_no_file():
    file_named = "no_file_name"
    result = open_json(file_named)
    assert result["error"].startswith("ERROR")
