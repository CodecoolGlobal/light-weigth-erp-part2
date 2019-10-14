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


list_labels=["Count1","Count2","Year","In/Out","Count3"]
title="Accounting"


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    
    special_functions=["(1) Show table", "(2) Add elements","(3) Remove element by it's ID","(4) Update an element","(5) Get which year has the highest profit","(6) Get what is the average (per item) profit in a given year?"]
    for i in range(len(special_functions)):
        print(special_functions[i])
    choice=ui.get_inputs(" ","What's your choose")
    table=data_manager.get_table_from_file("try.csv")

    if int(choice[0])==1: #show
        show_table(table)

    elif int(choice[0])==2: #add
        add(table)
        data_manager.write_table_to_file("try.csv",table)

    elif int(choice[0])==3: #remove
        id=ui.get_inputs(" ","Add the ID:")
        remove(table,id)
        data_manager.write_table_to_file("try.csv",table)

    elif int(choice[0])==4: #update
        id=ui.get_inputs(" ","Add the ID:")
        update(table,id)
        data_manager.write_table_to_file("try.csv",table)

    elif int(choice[0])==5: #max
        ui.print_result(which_year_max(table),"The max year: ")

    elif int(choice[0])==6: #avg
        year=ui.get_inputs(" ","Add the ID:")
        ui.print_result(avg_amount(table,year),f"The average in {year}: ")

    else:
        raise ValueError


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    for i in table:
        print(i)

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
    list_to_add=ui.get_inputs(list_labels,"Accounting")
    
    list_to_add.insert(0,common.generate_random(table))

    table.append(list_to_add)
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
    count=0
    searched_index=-1
    for i in table:
        if id_ in i:
            searched_index=count
            break
        count+=1
    print(searched_index)
    del table[searched_index]

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

    count=0
    searched_index=-1
    for i in table:
        if id_ in i:
            break
        count+=1
    
    to_change=ui.get_inputs(list_labels,title)
    to_change.insert(0,common.generate_random(table))
    table[count]=to_change

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

    income = 0
    spending = 0
    year_in_file = 3
    money_in_or_out = 4
    amount_of_money_in_or_out = 5
    
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
    print(year_and_its_profits)
    for key in year_and_its_profits:
        if year_and_its_profits[key] > max:
            max = year_and_its_profits[key]

    return max


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
    profit = 0
    income = 0
    spending = 0
    year_in_file = 3
    money_in_or_out = 4
    amount_of_money_in_or_out = 5
    items_count = 0
    for i in range(len(table)):
        if table[i][year_in_file] == str(year):
            if table[i][money_in_or_out] == "in":
                income += int(table[i][amount_of_money_in_or_out])
            elif table[i][money_in_or_out] == "out":
                spending += int(table[i][amount_of_money_in_or_out])
            items_count += 1

    profit = income - spending
    average_profit = profit/items_count
    return average_profit
