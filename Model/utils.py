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

def is_answer_ok(max_input):
    input_user = input("Enter your choice  : ")
    while not input_user.isnumeric() or not int(input_user) > 0 or not int(input_user) <= max_input:
        input_user = input("Please, Enter your choice : ")
    return int(input_user)

    # def is_answer_ok( user_input, max_input):
    #     while not user_input.isnumeric():
    #         user_input = input("Please, enter your choice : ")
    #     user_input = int(user_input)
    #     while user_input > 0 and user_input <= max_input:
    #         return user_input