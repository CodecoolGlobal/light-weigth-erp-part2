""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    oldest_date = 999999999

    born_year = 2
    name_of_person = 1

    list_of_oldest_persons_results = []


    for i in range(len(table)):
        if int(table[i][born_year]) < int(oldest_date):
            oldest_date = int(table[i][born_year])            
        if i > 0:
            if int(table[i][born_year]) == int(oldest_date):
                list_of_oldest_persons_results.append(str(table[i][name_of_person]))

    return list_of_oldest_persons_results

def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    # 1. calculate average age
    # 2. compare who is the closest to the average
    # 3. record their names in a "results" list
    
    born_year = 2
    name_of_person = 1

    overall = 0
    average_age = 0 #1973.1
    divider = 0
    list_of_persons_closest_to_average_results = []

    min = 999999999999
    for i in range(len(table)):
        years_in_table = int(table[i][born_year])
        overall += years_in_table
        divider += 1
    average_age = overall/divider

    for l in range(len(table)):
        comparing_value = abs((float(table[l][born_year]))-average_age)
        if min > comparing_value:
            min = comparing_value
            if l > 0:
                list_of_persons_closest_to_average_results.append(table[l][name_of_person])
        
    return list_of_persons_closest_to_average_results