""" Common module
implement commonly used functions here
"""

list_options = ["(1) Store manager","(2) Human resources manager","(3) Inventory manager",
    "(4) Accounting manager","(5) Sales manager","(6) Customer relationship management (CRM)",
    "(0) Exit program"]

import random
import ui

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    generated_list = []


    special_characters = "!@#$%^&*()[]{,}:"
    numbers = "1234567890"
    lowercase_letters = "qwertyuiopasdfghjklzxcvbnm"
    uppercase_letters = "qwertyuiopasdfghjklzxcvbnm".upper()



    return generated




def MAIN_MENU(title, list_options, exit_message):
    print(f"{title}: ")
    for row in list_options:
        print(row)
    user_input = ui.get_inputs(" ", "Your choice (type a number!):\n")
    if user_input == "0":
        print(exit_message)
