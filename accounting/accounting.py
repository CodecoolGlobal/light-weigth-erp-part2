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



list_labels=["Month of the transaction","Day of the transaction",
"Year of the transaction","in/out","Amount of transaction"]



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
    "Get which year has the highest profit",
    "Get what is the average profit in a given year?",
    "Go back to main menu"]

    table=data_manager.get_table_from_file("accounting/items_test.csv")
    ui.print_menu("Accounting Manager MENU",special_functions,"go back to Main Menu.")
    choice=ui.get_inputs(" ","What's your choose")
    choice=common.check_one_input_for_number(choice," ","What's your choose")
    

    if choice==1: #show, choice[0] because from the user inputs we get lists 
        show_table(table)

    elif choice==2: #add
        add(table)
        data_manager.write_table_to_file("accounting/items_test.csv",table)

    elif choice==3: #remove
        id=ui.get_inputs(" ","Add the searched ID")
        id=id[0]
        remove(table,id)
        data_manager.write_table_to_file("accounting/items_test.csv",table)

    elif choice==4: #update
        id=ui.get_inputs(" ","Add the searched ID")
        id=id[0]
        update(table,id)
        data_manager.write_table_to_file("accounting/items_test.csv",table)

    elif choice==5: #max
        ui.print_result(which_year_max(table),"The max profit's year: ")

    elif choice==6: #avg
        year=ui.get_inputs(" ","Add the year")
        year=year[0]
        result=avg_amount(table,year)
        if result!=None:
            ui.print_result(result,"The average profit in {0} is: ".format(year))

    elif choice==0: #main
        common.clear()

    else:
        ui.print_error_message("Wrong input!")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    ui.print_table(table,["ID","Count1","Count2","Date","in/out","Sold"])

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
    for key in year_and_its_profits:
        if year_and_its_profits[key] > max:
            max = year_and_its_profits[key]

    for key in year_and_its_profits:
        if year_and_its_profits[key]==max:
            return int(key)
                        


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
        if int(table[i][year_in_file]) == int(year):
            if table[i][money_in_or_out] == "in":
                income += int(table[i][amount_of_money_in_or_out])

            elif table[i][money_in_or_out] == "out":
                spending += int(table[i][amount_of_money_in_or_out])
            items_count += 1

    if items_count==0:
        ui.print_error_message("Nothing found in this year.")
    else:
        profit = income - spending
        average_profit = profit/items_count
        return average_profit