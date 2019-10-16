""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module(): # nem a MAIN MENU, ez csak az ACCOUNTING (part of it)!
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
   


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    print(table)


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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    table = table
    income = 0
    spending = 0
    year_in_file = 3
    money_in_or_out = 4
    amount_of_money_in_or_out = 5
     # 0 will be 2016 for example
    #van-e mar benne kulcs
    # kulcs = table[year_in_file]
    year_and_its_profits = {}
    
    profit_list = []
    profit = 0
    for i in range(len(table)):
        year_and_its_profits[table[i][year_in_file]] = profit
        for j in year_and_its_profits:
            if table[i][money_in_or_out] == "in" and table[i][year_in_file] == j:
                profit += int(table[i][amount_of_money_in_or_out])
                year_and_its_profits[j] = profit
            
            elif table[i][money_in_or_out] == "out" and table[i][year_in_file] == j:
                profit -= int(table[i][amount_of_money_in_or_out])
                year_and_its_profits[j] = profit

            else:
                pass
    max = -99999999
    for key in year_and_its_profits:
        if year_and_its_profits[key] > max:
            max = year_and_its_profits[key]
    print(year_and_its_profits[key][value])
    



def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    average_profit = 0
    table = table
    given_year = year
    profit = 0
    income = 0
    spending = 0
    year_in_file = 3
    money_in_or_out = 4
    amount_of_money_in_or_out = 5
    items_count = 0
    for i in range(len(table)):
        if table[i][year_in_file] == str(given_year):
            if table[i][money_in_or_out] == "in":
                income += int(table[i][amount_of_money_in_or_out])
            elif table[i][money_in_or_out] == "out":
                spending += int(table[i][amount_of_money_in_or_out])
            items_count += 1
    profit = income - spending
    average_profit = profit/items_count
    return average_profit # works


