import json
import csv
import datetime
import time
import unittest
from unittest.mock import patch
import pytest
from com_lib.file_processing import open_csv, open_json, save_csv, save_json, create_sample_files


class test_file_processing(unittest.TestCase):

    def test_create_sample_files(self):
        filename = 'test_sample'
        samplesize =  1000
        create_sample_files(filename, samplesize)
        result = open_csv(filename)
        assert(len(result) == samplesize - 1)

    def test_save_json(self):
        sample_dict = {"name": "bob", "date": str(datetime.datetime.now())}
        file_named = "test_1"
        json_data = []
        for i in range(1000):
            sample_dict = {"name": "bob", "date": str(datetime.datetime.now())}
            json_data.append(sample_dict)

        result = save_json(file_named, json_data)
        assert(result == "complete")


    def test_save_csv(self):
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
            assert(result == "complete")


    def test_open_json(self):
        file_named = "test_1"
        result = open_json(file_named)
        assert(len(result) > 1)


    def test_open_json_no_file(self):
        file_named = "no_file_name"
        result = open_json(file_named)
        assert(result["error"].startswith("ERROR"))


    def test_open_csv(self):
        file_named = "test_1"
        result = open_csv(file_named)
        assert(len(result) > 1)


    def test_open_json_no_file(self):
        file_named = "no_file_name"
        result = open_json(file_named)
        assert(result["error"].startswith("ERROR"))
