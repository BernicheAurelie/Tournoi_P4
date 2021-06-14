#! Python3
# coding: utf-8

from datetime import datetime


def is_date_valid(date_string): 
    format = "%m/%d/%Y"
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False

def register_end_time():
    end = datetime.now()
    end = end.strftime("%m/%d/%Y, %H:%M:%S")
    print(f"fin : {end}")
    return end