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
    common.clear()
    special_functions=["Show table",
    "Add elements",
    "Remove element by it's ID",
    "Update an element",
    "Get which items have not exceeded their durability yet",
    "Get the average durability times for each manufacturer",
    "Go back to main menu"]

    table=data_manager.get_table_from_file("inventory/inventory_test.csv")
    ui.print_menu("Human resources manager MENU",special_functions,"")
    choice=ui.get_inputs(" ","What's your choose")
    

    if int(choice[0])==1: #show, choice[0] because from the user inputs we get lists 
        show_table(table)

    elif int(choice[0])==2: #add
        add(table)
        data_manager.write_table_to_file("inventory/inventory_test.csv",table)

    elif int(choice[0])==3: #remove
        id=ui.get_inputs(" ","Add the ID")
        id=id[0]
        remove(table,id)
        data_manager.write_table_to_file("inventory/inventory_test.csv",table)

    elif int(choice[0])==4: #update
        id=ui.get_inputs(" ","Add the ID")
        id=id[0]
        update(table,id)
        data_manager.write_table_to_file("inventory/inventory_test.csv",table)

    elif int(choice[0])==5: #exceeded
        year=ui.get_inputs(" ","Give the year: ")
        year=int(year[0])
        ui.print_result(get_available_items(table,year)," ")

    elif int(choice[0])==6: #manufactures avg
        result=get_average_durability_by_manufacturers(table)
        ui.print_result(result,"")

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
    ui.print_table(table,["ID","Item name","Manufacturer","Purchase year","Durability"])


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

    final_dictionary = {}


    for i in range(len(table)):
        if table[i][manufacturer] in final_dictionary:
            final_dictionary[table[i][manufacturer]]+=int(table[i][durability])
        else:
            final_dictionary[table[i][manufacturer]]=int(table[i][durability])
        

    '''final_dictionary[table[i][manufacturer]] = average_durability
        
            if table[i][manufacturer] in final_dictionary:
                g = int(table[i][durability])
                final_dictionary[table[i][manufacturer]] += g

        for l in final_dictionary:
            if table[i][manufacturer] == final_dictionary[l]:
                adding_durability += int(table[i][durability])
                divider += int(table[i][manufacturer])'''

    dictionary_count={}
    for l in final_dictionary:
        dictionary_count[l]=0

    for i in range(len(table)):
        for l in dictionary_count:
            if l==table[i][manufacturer]:
                dictionary_count[table[i][manufacturer]]+=1
    
    for l in final_dictionary:
        final_dictionary[l]=int(final_dictionary[l])/int(dictionary_count[l])
    
    print(final_dictionary)
    return(final_dictionary)

a=data_manager.get_table_from_file("inventory/inventory_test.csv")
get_average_durability_by_manufacturers(a)
