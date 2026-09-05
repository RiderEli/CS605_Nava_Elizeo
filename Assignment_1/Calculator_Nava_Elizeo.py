# [Nava, Elizeo]
# [September 2, 2026]
# [Updated: 9/2/26]
# [This is a Python code for a simple calculator]

## Different Codes
first_number = "Enter your first number: "
second_number = "Enter your second number: "

import time

def start_calculator():
    print("Welcome to the Calculator")
    time.sleep(2)

def calculation_int():
    print("------------------------------------------------------------------------")
    num1st = str(input(first_number))
    num2nd = str(input(second_number))

    try:
        intnumber_first = int(num1st)
        intnumber_second = int(num2nd)

        while intnumber_first != intnumber_second or intnumber_first == intnumber_second:
            print("-----------------------------------------------------------------------")
            operation_input = input("Would you like to add, subtract, multiply or divide?")
            if operation_input == "add" or operation_input == " add":
                addition = intnumber_first + intnumber_second
                print(f'{intnumber_first} + {intnumber_second} = {addition}')
                recalculate()
                break
            elif operation_input == "subtract" or operation_input == " subtract":
                subtraction = intnumber_first - intnumber_second
                print(f'{intnumber_first} - {intnumber_second} = {subtraction}')
                recalculate()
                break
            elif operation_input == "multiply" or operation_input == " multiply":
                multiplication = intnumber_first * intnumber_second
                print(f'{intnumber_first} * {intnumber_second} = {multiplication}')
                recalculate()
                break
            elif operation_input == "divide" or operation_input == " divide":
                division = intnumber_first / intnumber_second
                print(f'{intnumber_first} / {intnumber_second} = {division}')
                recalculate()
                break
            else:
                print("Please enter a valid input")

    except ValueError:
        print("Please enter numbers, not letters.")
        calculation_int()

def calculation_float():
    print("------------------------------------------------------------------------")
    num1st = str(input(first_number))
    num2nd = str(input(second_number))

    try:
        floatnumber_first = float(num1st)
        floatnumber_second = float(num2nd)

        while floatnumber_first != floatnumber_second or floatnumber_first == floatnumber_second:
            print("------------------------------------------------------------------------")
            operation_input = input("Would you like to add, subtract, multiply or divide?")
            if operation_input == " add" or operation_input == "add":
                addition = floatnumber_first + floatnumber_second
                print(f'{floatnumber_first} + {floatnumber_second} = {addition}')
                recalculate()
                break
            elif operation_input == " subtract" or operation_input == "subtract":
                subtraction = floatnumber_first - floatnumber_second
                print(f'{floatnumber_first} - {floatnumber_second} = {subtraction}')
                recalculate()
                break
            elif operation_input == " multiply" or operation_input == "multiply":
                multiplication = floatnumber_first * floatnumber_second
                print(f'{floatnumber_first} * {floatnumber_second} = {multiplication}')
                recalculate()
                break
            elif operation_input == " divide" or operation_input == "divide":
                division = floatnumber_first / floatnumber_second
                print(f'{floatnumber_first} / {floatnumber_second} = {division}')
                recalculate()
                break
            else:
                print("Please enter a valid input")

    except ValueError:
        print("Please enter numbers, not letters.")
        calculation_float()

def recalculate():
    print("------------------------------------------------------------------------")
    recalculate_ = input("Would you like to recalculate? yes/no")
    if recalculate_ == "yes" or recalculate_ == " yes":
        int_or_float_select()
    elif recalculate_ == "no" or recalculate_ == " no":
        print("Thank you for using this calculator")
        time.sleep(2)
        print("This program has been turned off")
    else:
        print("Please enter a valid input")
        recalculate()

def int_or_float_select():
    print("------------------------------------------------------------------------")
    select_input = input("Would you like to calculate decimals? yes/no")
    if select_input == "yes" or select_input == " yes":
        calculation_float()
    elif select_input == "no" or select_input == " no":
        calculation_int()
    else:
        print("Please enter a valid input")
        int_or_float_select()

## Where the codes are performing from.
start_calculator()
int_or_float_select()