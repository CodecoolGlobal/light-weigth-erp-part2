""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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
    "Get items sold between two dates",
    "Go back to main menu"]

    table=data_manager.get_table_from_file("sales/sales_test.csv")
    ui.print_menu("Accounting manager MENU",special_functions,"")
    choice=ui.get_inputs(" ","What's your choose")
    

    if int(choice[0])==1: #show, choice[0] because from the user inputs we get lists 
        show_table(table)

    elif int(choice[0])==2: #add
        add(table)
        data_manager.write_table_to_file("sales/sales_test.csv",table)

    elif int(choice[0])==3: #remove
        id=ui.get_inputs(" ","Add the ID")
        id=id[0]
        remove(table,id)
        data_manager.write_table_to_file("sales/sales_test.csv",table)

    elif int(choice[0])==4: #update
        id=ui.get_inputs(" ","Add the ID")
        id=id[0]
        update(table,id)
        data_manager.write_table_to_file("sales/sales_test.csv",table)

    elif int(choice[0])==5: #lowest price item id
        ui.print_result(get_lowest_price_item_id(table),"")

    elif int(choice[0])==6: #avg
        list=["day","month","year"]
        date1=[]
        date2=[]
        for i in range(3):
            date1.append(ui.get_inputs(" ","Add the first date's {}".format(list[i])))

        for i in range(3):
            date2.append(ui.get_inputs(" ","Add the second date's {}".format(list[i])))

        result=get_items_sold_between(table,date1[0][0],
        date1[1][0],date1[2][0],date2[0][0],date2[1][0],date2[2][0])

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
    
    to_change=ui.get_inputs(list_labels,title)
    to_change.insert(0,common.generate_random(table))
    table[searched_index]=to_change

    return table


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
