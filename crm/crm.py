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
    "Get subscribed e-mails",
    "Go back to main menu"]

    table=data_manager.get_table_from_file("crm/customers_test.csv")
    ui.print_menu("Customer Relationship Management MENU",special_functions,"")
    choice=ui.get_inputs(" ","What's your choose")
    

    if int(choice[0])==1: #show, choice[0] because from the user inputs we get lists 
        show_table(table)

    elif int(choice[0])==2: #add
        add(table)
        data_manager.write_table_to_file("crm/customers_test.csv",table)

    elif int(choice[0])==3: #remove
        id=ui.get_inputs(" ","Add the searched ID")
        id=id[0]
        remove(table,id)
        data_manager.write_table_to_file("crm/customers_test.csv",table)

    elif int(choice[0])==4: #update
        id=ui.get_inputs(" ","Add the searched ID")
        id=id[0]
        update(table,id)
        data_manager.write_table_to_file("crm/customers_test.csv",table)

    elif int(choice[0])==5: #ID cust
        ui.print_result(get_longest_name_id(table),"The ID of the customer is:")

    elif int(choice[0])==6: #subscribed
        result=get_subscribed_emails(table)
        ui.print_result(result,"These customers have subscribed to the news letter:")

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
        table (list): list in which record should be updated
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
    
    if searched_index!=-1:
        to_change=ui.get_inputs(list_labels,"")
        to_change.insert(0,common.generate_random(table))
        table[searched_index]=to_change

        return table
    else:
        raise ValueError


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

    # WORKS


