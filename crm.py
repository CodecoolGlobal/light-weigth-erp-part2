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


