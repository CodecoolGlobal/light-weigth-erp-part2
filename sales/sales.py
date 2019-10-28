""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

list_labels=["Title","Price","Month","Day","Year"]

id=0
title=1
price=2
month=3
day=4
year=5


month_to_day = {1: 31, 2: 28, 3:31, 4: 30, 5:31, 6:30, 7:31,
 8:31, 9:30, 10:31, 11: 30, 12: 31}

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
    "Get lowest price ID",
    "Get items sold between two dates"]

    table=data_manager.get_table_from_file("sales/sales_test.csv")
    ui.print_menu("Sales Manager MENU",special_functions,"")
    choice=ui.get_inputs(" ","What's your choice?")
    choice=common.check_one_input_for_number(choice," ","What's your choice?")
    
    while choice!=0:
        if choice==1: #show, choice[0] because from the user inputs we get lists 
            show_table(table)

        elif choice==2: #add
            add(table)
            data_manager.write_table_to_file("sales/sales_test.csv",table)

        elif choice==3: #remove
            id=ui.get_inputs(" ","Add the searched ID")
            id=id[0]
            remove(table,id)
            data_manager.write_table_to_file("sales/sales_test.csv",table)

        elif choice==4: #update
            id=ui.get_inputs(" ","Add the searched ID")
            id=id[0]
            update(table,id)
            data_manager.write_table_to_file("sales/sales_test.csv",table)

        elif choice==5: #lowest price item id
            ui.print_result(get_lowest_price_item_id(table),"The ID of the item that was sold for the lowest price is:")

        elif choice==6: #avg
            list=["year","month","day"]
            date1=[]
            date2=[]
            for i in range(3):
                value=int(ui.get_inputs(" ","Add the first date's {}".format(list[i]))[0])

                if i==0: # years
                    while not(value>0):
                    
                        ui.print_error_message("Wrong attribute")
                        value=ui.get_inputs(" ","Add the first date's {}".format(list[i]))
                        value=common.check_one_input_for_number(value," ","Add the first date's {}".format(list[i]))
                    date1.append(value)

                elif i==1: #months
                    while not(value>0) or not(value<13):
                        ui.print_error_message("Wrong attribute")
                        value=ui.get_inputs(" ","Add the first date's {}".format(list[i]))
                        value=common.check_one_input_for_number(value," ","Add the first date's {}".format(list[i]))
                    date1.append(value)

                elif i==2: # days
                    if common.leap_year_checker(date1[0]) is True:
                        month_to_day[2] = 29
                    while not(value>0) or not(value <= month_to_day[date1[1]]):
                        ui.print_error_message("Wrong attribute")
                        value=ui.get_inputs(" ","Add the first date's {}".format(list[i]))
                        value=common.check_one_input_for_number(value," ","Add the first date's {}".format(list[i]))
                    date1.append(value)
                    month_to_day[2] = 28
            for i in range(3):
                value=ui.get_inputs(" ","Add the second date's {}".format(list[i]))
                value=common.check_one_input_for_number(value," ","Add the second date's {}".format(list[i]))
                if i==0:
                    while not(value>0):
                    
                        ui.print_error_message("Wrong attribute")
                        value=ui.get_inputs(" ","Add the second date's {}".format(list[i]))
                        value=common.check_one_input_for_number(value," ","Add the second date's {}".format(list[i]))
                    date2.append(value)

                elif i==1:
                    while not(value>0) or not(value<13):
                        ui.print_error_message("Wrong attribute")
                        value=ui.get_inputs(" ","Add the second date's {}".format(list[i]))
                        value=common.check_one_input_for_number(value," ","Add the second date's {}".format(list[i]))
                    date2.append(value)

                elif i==2:
                    if common.leap_year_checker(int(date2[0])) == True:
                        month_to_day[2] = 29
                    while not(value>0) or not(value <= month_to_day[date1[1]]):
                        ui.print_error_message("Wrong attribute")
                        value=ui.get_inputs(" ","Add the second date's {}".format(list[i]))
                        value=common.check_one_input_for_number(value," ","Add the second date's {}".format(list[i]))
                        
                    date2.append(value)
                    month_to_day[2] = 28
            result=get_items_sold_between(table,date1[1],
            date1[2],date1[0],date2[1],date2[2],date2[0])

            ui.print_result(result,"These items are sold between the given dates:")

        else:
            raise ValueError

        ui.print_menu("Sales Manager MENU",special_functions,"")
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

    ui.print_table(table,["ID","Title","Price","Month","Day","Year"])


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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    lowest_price=int(table[0][price])
    lowest_price_id=table[0][id]
    for i in range(len(table)):
        if int(table[i][price])<int(lowest_price):
            lowest_price=table[i][price]
            lowest_price_id=table[i][id]

    return lowest_price_id

    


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    result=[]
    for i in range(len(table)):
        if((int(table[i][year])>int(year_from)) and (int(table[i][year])<int(year_to))):
            result.append(table[i])

        elif ((int(table[i][year])==int(year_from)) or (int(table[i][year])==int(year_to))):
            if((int(table[i][month])>int(month_from)) and (int(table[i][month])<int(month_to))):
                result.append(table[i])

            elif((int(table[i][month])==int(month_from)) or (int(table[i][month])==int(month_to))):
                if((int(table[i][day])>int(day_from)) and (int(table[i][day])<int(day_to))):
                    result.append(table[i])

    for i in range(len(result)):
        result[i][price]=int(result[i][price])
        result[i][day]=int(result[i][day])
        result[i][month]=int(result[i][month])
        result[i][year]=int(result[i][year])

    return result
    # your code


# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    # your code


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    # your code


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    table=data_manager.get_table_from_file("sales/sales_test.csv")

    customer_id=-1

    list_of_elements={}
    list_of_elements=set(list_of_elements)

    for row in table:
        list_of_elements.add(row[customer_id])

    return list_of_elements


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    customer_id=-1

    list_of_elements={}
    list_of_elements=set(list_of_elements)

    for row in table:
        list_of_elements.add(row[customer_id])

    return list_of_elements




def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    table=data_manager.get_table_from_file("sales/sales_test.csv")

    dictionary={}
    customer_id=0

    for row in table:
        if not(row[-1] in dictionary):
            dictionary[row[-1]]=[]

    sale_ids=[]

    
    for elements in dictionary:
        for row in table:
            if row[-1]==elements:
                sale_ids.append(row[customer_id])
        dictionary[elements]=sale_ids
        sale_ids=[]

    return dictionary


def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    dictionary={}
    customer_id=0

    for row in table:
        if not(row[-1] in dictionary):
            dictionary[row[-1]]=[]

    sale_ids=[]

    
    for elements in dictionary:
        for row in table:
            if row[-1]==elements:
                sale_ids.append(row[customer_id])
        dictionary[elements]=sale_ids
        sale_ids=[]

    return dictionary



def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    table=data_manager.get_table_from_file("sales/sales_test.csv")
    
    customer_id=6

    dictionary={}

    for row in table:
        if row[customer_id] in dictionary:
            dictionary[row[customer_id]]+=1
        else:
            dictionary[row[customer_id]]=1

    return dictionary



def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """
    customer_id=6

    dictionary={}

    for row in table:
        if row[customer_id] in dictionary:
            dictionary[row[customer_id]]+=1
        else:
            dictionary[row[customer_id]]=1

    return dictionary
    
