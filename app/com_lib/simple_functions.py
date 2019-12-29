# -*- coding: utf-8 -*-
from datetime import datetime


def get_current_datetime() -> datetime:
    """
    get the current datetime

    Returns:
        datetime.now()
    """
    current_time: datetime = datetime.now()
    return current_time


def month_from_number(number: int) -> str:
    min_value = 1
    max_value = 12

    if isinstance(number, bool):
        result = f"Invalid: Must be an integer and not type of {type(number)}"
    elif isinstance(number, int) == False:
        # error if not an integer
        result = f"Invalid: Must be an integer and not type of {type(number)}"

    elif number < min_value:
        # error if less than 1
        result = f"Invalid: Value of input ({number}) is less than 1"

    elif number > max_value:
        # error if greater than 12
        result = f"Invalid: Value of input ({number}) is greater than 12"

    else:
        # retrieve month name
        month = {
            1: "January",
            2: "Febuary",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        }
        result = month.get(number)

    return result


if __name__ == "__main__":
    num = [False, "a", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1.1, 1.0]
    for i in num:
        result = month_from_number(i)
        print(result)
