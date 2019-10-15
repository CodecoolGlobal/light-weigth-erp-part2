""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # 1. Add year + durability = max durability
    # 2. Compare max durability to year ( if max durability > or = to year)

    release_year = 3
    durability = 4
    max_durability = 0
    not_exceeded_max_durability = []
    add = 0

    for i in range(len(table)):
        max_durability = int(table[i][release_year]) + int(table[i][durability])
        table[i][release_year] = int(table[i][release_year])
        table[i][durability] = int(table[i][durability])
        if year <= int(max_durability):
            not_exceeded_max_durability.append(table[i])
        if year > int(max_durability):
            break
        max_durability = 0

    return not_exceeded_max_durability

def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # 1. Calculate average durability
    # 2. Record average durability for EACH manufacturer
    # 3. Put it into a dictionary
    
    manufacturer = 2
    durability = 4

    max_durability = 0
    average_durability = 0
    adding_durability = 0
    divider = 0

    final_dictionary = {}


    for i in range(len(table)):
        final_dictionary[table[i][manufacturer]] = average_durability
        if key in final_dictionary.items() == table[i][manufacturer]:
            adding_durability += int(table[i][durability])
            divider += 1
