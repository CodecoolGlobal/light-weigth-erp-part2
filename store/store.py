""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

list_labels=["Title","Manufacturer","Price","In stock"]

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    common.clear()
    special_functions=["Show table",
    "Add elements",
    "Remove element by it's ID",
    "Update an element",
    "Get ",
    "Get ",
    "Go back to main menu"]

    table=data_manager.get_table_from_file("store/games_test.csv")
    ui.print_menu("Accounting manager MENU",special_functions,"")
    choice=ui.get_inputs(" ","What's your choose")
    

    if int(choice[0])==1: #show, choice[0] because from the user inputs we get lists 
        show_table(table)

    elif int(choice[0])==2: #add
        add(table)
        data_manager.write_table_to_file("store/games_test.csv",table)

    elif int(choice[0])==3: #remove
        id=ui.get_inputs(" ","Add the ID")
        id=id[0]
        remove(table,id)
        data_manager.write_table_to_file("store/games_test.csv",table)

    elif int(choice[0])==4: #update
        id=ui.get_inputs(" ","Add the ID")
        id=id[0]
        update(table,id)
        data_manager.write_table_to_file("store/games_test.csv",table)

    elif int(choice[0])==5: #max
        ui.print_result(which_year_max(table),"The max year: ")

    elif int(choice[0])==6: #avg
        year=ui.get_inputs(" ","Add the year")
        year=year[0]
        result=avg_amount(table,year)
        if result!=None:
            ui.print_result(result,"The average in {0}: ".format(year))

    elif int(choice[0])==7: #main
        common.clear()

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

    ui.print_table(table,["ID","Title","Manufacturer","Price","In stock"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    list_to_add=ui.get_inputs(list_labels,"")
    
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
        if i[0]==id_:
            searched_index=count
        count+=1
    table.pop(searched_index)
    
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    count=0
    searched_index=-1
    for i in table:
        if i[0]==id_:
            searched_index=count
        count+=1
    
    to_change=ui.get_inputs(list_labels,title)
    to_change.insert(0,common.generate_random(table))
    table[searched_index]=to_change

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
