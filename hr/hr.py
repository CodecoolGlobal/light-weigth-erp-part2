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


list_labels=["Name","Born year"]


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
    "Get oldest person",
    "Get person whose closest to averege",
    "Go back to main menu"]

    table=data_manager.get_table_from_file("hr/persons_test.csv")
    ui.print_menu("Human Resources Manager MENU",special_functions,"go back to Main Menu.")
    choice=ui.get_inputs(" ","What's your choice?")
    choice=common.check_one_input_for_number(choice," ","What's your choice?")
    

    if choice==1: #show
        show_table(table)

    elif choice==2: #add
        add(table)
        data_manager.write_table_to_file("hr/persons_test.csv",table)

    elif choice==3: #remove
        id=ui.get_inputs(" ","Add the searched ID")
        id=id[0]
        remove(table,id)
        data_manager.write_table_to_file("hr/persons_test.csv",table)

    elif choice==4: #update
        id=ui.get_inputs(" ","Add the searched ID")
        id=id[0]
        update(table,id)
        data_manager.write_table_to_file("hr/persons_test.csv",table)

    elif choice==5: #oldest
        ui.print_result(get_oldest_person(table),"The oldest persons are:")

    elif choice==6: #closest to avg
        result=avg_amount(table,year)
        ui.print_result(result,"The person closest to average is:")

    elif choice==0: #main
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

    ui.print_table(table,["ID","Name","Born in"])


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
    average_age = 0 
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
