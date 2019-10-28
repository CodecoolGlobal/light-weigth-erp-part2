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

list_labels=["Item name","Manufacturer","Purchase year","Durability"]

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
    "Get the average durability times for each manufacturer"]

    table=data_manager.get_table_from_file("inventory/inventory_test.csv")
    ui.print_menu("Inventory Manager MENU",special_functions,"go back to Main Menu.")
    choice=ui.get_inputs(" ","What's your choice?")
    choice=common.check_one_input_for_number(choice," ","What's your choice?")
    
    while choice!=0:
        if choice==1: #show, choice[0] because from the user inputs we get lists 
            show_table(table)

        elif choice==2: #add
            add(table)
            data_manager.write_table_to_file("inventory/inventory_test.csv",table)

        elif choice==3: #remove
            id=ui.get_inputs(" ","Add the searched ID")
            id=id[0]
            remove(table,id)
            data_manager.write_table_to_file("inventory/inventory_test.csv",table)

        elif choice==4: #update
            id=ui.get_inputs(" ","Add the searched ID")
            id=id[0]
            update(table,id)
            data_manager.write_table_to_file("inventory/inventory_test.csv",table)

        elif choice==5: #exceeded
            year=ui.get_inputs(" ","Give the year")
            year=common.check_one_input_for_number(year," ","Give the year")
            ui.print_result(get_available_items(table,year),"These items that not exceeded their durability yet:")

        elif choice==6: #manufactures avg
            result=get_average_durability_by_manufacturers(table)
            ui.print_result(result,"The average durability times for each manufaturer is:")

        else:
            raise ValueError
        
        ui.print_menu("Inventory Manager MENU",special_functions,"go back to Main Menu.")
        choice=ui.get_inputs(" ","What's your choice?")
        choice=common.check_one_input_for_number(choice," ","What's your choice?")
        common.clear()

    common.clear()


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
    in_it=False
    for i in table:
        if i[0]==id_:
            searched_index=count
            in_it=True
        count+=1

    if in_it:    
        table.pop(searched_index)
    else:
        ui.print_error_message("ID not found")
    
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
    in_it=False
    for i in table:
        if i[0]==id_:
            searched_index=count
            in_it=True
        count+=1
    
    if in_it:
        to_change=ui.get_inputs(list_labels,"")
        to_change.insert(0,common.generate_random(table))
        table[searched_index]=to_change

        return table
    
    else:
        ui.print_error_message("ID is not found")


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


    not_exceeded_max_durability = []


    for i in range(len(table)):
        max_durability = table[i][release_year] + table[i][durability]
        if year <= max_durability:
            not_exceeded_max_durability.append(table[i][name_of_console])

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

    dictionary_count={}
    for l in final_dictionary:
        dictionary_count[l]=0

    for i in range(len(table)):
        for l in dictionary_count:
            if l==table[i][manufacturer]:
                dictionary_count[table[i][manufacturer]]+=1
    
    for l in final_dictionary:
        final_dictionary[l]=int(final_dictionary[l])/int(dictionary_count[l])
    
    return final_dictionary
