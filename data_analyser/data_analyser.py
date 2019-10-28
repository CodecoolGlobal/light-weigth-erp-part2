"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoid using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    

    common.clear()
    special_functions=["Latest buyer name",
    "Last buyer ID",
    "The buyer name spent most and the money spent",
    "Get the buyer id spent most and the money spent",
    "Get the most frequent buyers names",
    "Get the most frequent buyers ids"]

    table=data_manager.get_table_from_file("data_analyser/data_analyser.csv")
    ui.print_menu("Data Analyser MENU",special_functions,"go back to Main Menu.")
    choice=ui.get_inputs(" ","What's your choice?")
    choice=common.check_one_input_for_number(choice," ","What's your choice?")
    
    '''while choice!=0:
        if choice==1:  
            

        elif choice==2: 
            

        elif choice==3: 
            

        elif choice==4:
            

        elif choice==5: 
            

        elif choice==6: 
            

        else:
            raise ValueError
    '''
        
    ui.print_menu("Data Analyser MENU",special_functions,"go back to Main Menu.")
    choice=ui.get_inputs(" ","What's your choice?")
    choice=common.check_one_input_for_number(choice," ","What's your choice?")
    common.clear()

    common.clear()



def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """
    return crm.get_name_by_id(get_the_last_buyer_id())


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """
    return sales.get_customer_id_by_sale_id(sales.get_item_id_sold_last())
    


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    tmp = []
    dictionary = sales.get_all_sales_ids_for_customer_ids()
    for key, value in dictionary.items():
        if not tmp:
            tmp.append((key, sales.get_the_sum_of_prices(value)))
        elif sales.get_the_sum_of_prices(value) > tmp[0][1]:
            tmp[0] = (key, sales.get_the_sum_of_prices(value))

    return (crm.get_name_by_id(tmp[0][0]),tmp[0][1])

def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    tmp = []
    dictionary = sales.get_all_sales_ids_for_customer_ids()
    for key, value in dictionary.items():
        if not tmp:
            tmp.append((key, sales.get_the_sum_of_prices(value)))
        elif sales.get_the_sum_of_prices(value) > tmp[0][1]:
            tmp[0] = (key, sales.get_the_sum_of_prices(value))

    return (tmp[0][0],tmp[0][1])


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    tmp = []
    tmp_ordered = []
    dictionary = sales.get_num_of_sales_per_customer_ids()
    for key, value in dictionary.items():
        tmp.append((crm.get_name_by_id(key), value))

    while tmp:
        maximum_value = tmp[0][1]
        maximum = tmp[0]
        for i in range(len(tmp)):
            if tmp[i][1] > maximum_value:
                maximum_value = tmp[i][1]
                maximum = tmp[i]
        tmp_ordered.append(maximum)
        tmp.remove(maximum)
        if len(tmp_ordered) == num:
            return(tmp_ordered)

def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    tmp = []
    tmp_ordered = []
    dictionary = sales.get_num_of_sales_per_customer_ids()
    for key, value in dictionary.items():
        tmp.append((key, value))

    while tmp:
        maximum_value = tmp[0][1]
        maximum = tmp[0]
        for i in range(len(tmp)):
            if tmp[i][1] > maximum_value:
                maximum_value = tmp[i][1]
                maximum = tmp[i]
        tmp_ordered.append(maximum)
        tmp.remove(maximum)
        if len(tmp_ordered) == num:
            return(tmp_ordered)
