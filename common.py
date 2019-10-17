""" Common module
implement commonly used functions here
"""

import random
import ui
import data_manager
import os

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

    statement=True
    while statement:
        char_list=[]
        generated =[]
        char_list.append("'\"+!%/=()\|€÷×[]$<>#&@{},?.:-*")
        char_list.append("0123456789")
        char_list.append("qwertzuiopasdfghjklíyxcvbnm")
        char_list.append("qwertzuiopasdfghjklíyxcvbnm".upper())
        count=0
        for i in range(len(char_list)):
            while count<2:
                generated.append(random.choice(char_list[i]))
                count+=1
            count=0

        random.shuffle(generated)
        
        generated="".join(generated)
        for i in table:
            if not(generated in i):
                statement=False

    return generated

def clear():
    os.system("clear")

def check_one_input_for_number(list,list_labels,title):
    value=list[0]
    statement=False
    
    while(statement!=True):
        try:
            value=int(list[0])
            statement=True
        except:
            ui.print_error_message("Wrong input!")
            value=ui.get_inputs(list_labels,title)

    return value


def leap_year_checker(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year / 400 == 0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False
