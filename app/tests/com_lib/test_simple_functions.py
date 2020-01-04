# -*- coding: utf-8 -*-
# import json
# import csv
import datetime
import unittest

from com_lib.simple_functions import get_current_datetime
from com_lib.simple_functions import month_from_number


class Test(unittest.TestCase):
    def test_get_current_datetime(self):
        result = get_current_datetime()
        assert type(result) is datetime.datetime

    def test_month_from_number(self):
        number = 1
        result = month_from_number(number)
        assert result == "January"

    def test_month_from_number_error_bool(self):
        number = True
        result = month_from_number(number)
        assert result.startswith("Invalid:")

    def test_month_from_number_error_float(self):
        number = 1.1
        result = month_from_number(number)
        assert result.startswith("Invalid:")

    def test_month_from_number_error_min(self):
        number = 0
        result = month_from_number(number)
        assert result.startswith("Invalid:")

    def test_month_from_number_error_max(self):
        number = 13
        result = month_from_number(number)
        assert result.startswith("Invalid:")
