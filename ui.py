""" User Interface (UI) module """
list_options = ["(1) Store manager","(2) Human resources manager","(3) Inventory manager",
    "(4) Accounting manager","(5) Sales manager","(6) Customer relationship management (CRM)",
    "(0) Exit program"]

def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    list_of_nametags=[]
    for i in table[0]:
        list_of_nametags.append(len(i))

    for i in range(len(table)):
        for j in range(len(table[i])):
            for k in range(len(table)):
                if len(table[k][j])>list_of_nametags[j]:
                    list_of_nametags[j]=len(table[k][j])

    for i in range(len(list_of_nametags)):
        if list_of_nametags[i]<len(title_list[i]):
            list_of_nametags[i]=len(title_list[i])


    sum_spaces=0
    for i in range(len(list_of_nametags)):
        sum_spaces+=list_of_nametags[i]+2+1
    

    print("/"+(sum_spaces*"-")+"\\")
    print(" |",end="")
    for i in range(len(title_list)):
        to_size=list_of_nametags[i]
        print("{0:^{1}}".format(title_list[i],to_size),end="")
        print(" | ",end="")
    print()
    print(" |"+((sum_spaces-2)*"-")+"|")


    print(" |",end="")
    for i in range(len(table)):
        for j in range(len(table[i])):
            to_size=list_of_nametags[j]
            print("{0:^{1}}".format(table[i][j],to_size),end="")
            print(" | ",end="")
        print()
        
        if i<len(table)-1:
            print(" |"+((sum_spaces-2)*"-")+"|")
            print(" |",end="")
    print("\\"+(sum_spaces*"-")+"/")

def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    
    print(label,result)


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    count=1
    print("\t"+"\t",title)
    for i in list_options:
        char_c=str(count)
        print("("+char_c+")",i)
        count+=1


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """


    inputs = []
    for i in range(len(list_labels)): 
        a=input("{} {}: " .format(title,list_labels[i]))
        inputs.append(a)

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print("ERROR: ",message)
