from data_manager import get_table_from_file
def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    table = get_table_form_file("items.csv")
    print(table)
table = get_table_from_file("items.csv")
show_table(table)