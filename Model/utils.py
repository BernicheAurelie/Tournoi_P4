#! Python3
# coding: utf-8

from datetime import datetime


"""Some functions define for differentes classes"""


def is_date_valid(date_string):
    """Check date format to serialize it"""
    format = "%m/%d/%Y"
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False


def register_time():
    """Register time and adapts it to serialization"""
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")
    return time


def is_answer_ok(max_input):
    """Check validity of the user answer.
    It must be an number in the given range"""
    input_user = input("Enter your choice  : ")
    while (
        not input_user.isnumeric()
        or not int(input_user) > 0
        or not int(input_user) <= max_input
    ):
        input_user = input("Please, Enter your choice : ")
    return int(input_user)
