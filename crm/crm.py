""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

list_labels=["Name","e-mail","Subscribed"]


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
    "Update an element by it's ID",
    "Get longest name ID",
    "Get subscribed e-mails"]

    table=data_manager.get_table_from_file("crm/customers_test.csv")
    ui.print_menu("Customer Relationship Management MENU",special_functions,"go back to Main Menu.")
    choice=ui.get_inputs(" ","What's your choice?")
    choice=common.check_one_input_for_number(choice," ","What's your choice?")
    
    while choice!=0:
        if choice==1: #show, choice[0] because from the user inputs we get lists 
            show_table(table)

        elif choice==2: #add
            add(table)
            data_manager.write_table_to_file("crm/customers_test.csv",table)

        elif choice==3: #remove
            id=ui.get_inputs(" ","Add the searched ID")
            id=id[0]
            remove(table,id)
            data_manager.write_table_to_file("crm/customers_test.csv",table)

        elif choice==4: #update
            id=ui.get_inputs(" ","Add the searched ID")
            id=id[0]
            update(table,id)
            data_manager.write_table_to_file("crm/customers_test.csv",table)

        elif choice==5: #ID cust
            ui.print_result(get_longest_name_id(table),"The ID of the customer is:")

        elif choice==6: #subscribed
            result=get_subscribed_emails(table)
            ui.print_result(result,"These customers have subscribed to the news letter:")

        else:
            ui.print_error_message("Wrong input!")

        ui.print_menu("Customer Relationship Management MENU",special_functions,"go back to Main Menu.")
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

    ui.print_table(table,["ID","Name","e-mail","Subscribed"])


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

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    # 1. find customer with longest name
    # 2. record ID of customer with longest name
    # 3. Alphabetical order

    id = 0
    name = 1

    max_name_length = 0
    ID_of_longest_name = ""
    longest_names_dictionary = {}
    longest_names = []
    id_of_longest_names = []

    for i in range(len(table)):
        if max_name_length < len(table[i][name]):
            max_name_length = len(table[i][name])

    for i in range(len(table)):
        if len(table[i][name]) >= max_name_length:
            longest_names_dictionary[table[i][id]] = [table[i][name]]
        
    for i, j in longest_names_dictionary.items():
        longest_names.append(j)
        id_of_longest_names.append(i)
    
    for i in range(len(longest_names)):
        for j in range(len(longest_names)):
            if longest_names[i] < longest_names[j]:
                temp = longest_names[i]
                longest_names[i] = longest_names[j]
                longest_names[j] = temp
                temp2 = id_of_longest_names[i]
                id_of_longest_names[i] = id_of_longest_names[j]
                id_of_longest_names[j] = temp2 

    
    
    return id_of_longest_names[len(longest_names)-1]




def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

        # the question: Which customers has subscribed to the newsletter?
        # return type: list of strings (where string is like email+separator+name, separator=";")

    subscription_status = 3
    email = 2
    name = 1

    subscirbed_people_list = []

    for i in range(len(table)):
        if int(table[i][subscription_status]) == 1:
            string = table[i][email]+";"+table[i][name]
            subscirbed_people_list.append(string)
    return subscirbed_people_list
    # your code


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    id_index=0
    name=1

    table=data_manager.get_table_from_file("crm/customers_test.csv")
    for row in range(len(table)):
        if table[row][id_index]==id:
            return table[row][name]



def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """
    id_index=0
    name=1

    for row in range(len(table)):
        if table[row][id_index]==id:
            return table[row][name]

def get_all_ids():
    customer_id = 0
    table=data_manager.get_table_from_file("crm/customers_test.csv")
    list_of_ids = []
    for i in range(len(table)):
        list_of_ids.append(table[i][customer_id])

    return list_of_ids