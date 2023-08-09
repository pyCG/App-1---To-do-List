FILE_PATH = "/Users/gui/Documents/Course Python/todos.txt"


def get_todos(file_path=FILE_PATH):
    """
    Read a text file and return a list of to-do items.
    
    Args:
        file_path (str, optional): _description_. Defaults to "todos.txt".

    Returns:
        _type_: _description_
    """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, file_path=FILE_PATH):
    """ Write on a text file a list of to-do items.

    Args:
        todos_arg (_type_): _description_
        file_path (str, optional): _description_. Defaults to 'todos.txt'.
    """
    with open(file_path, 'w') as file:
            file.writelines(todos_arg)