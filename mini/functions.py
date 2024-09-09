FILENAME = "test_files/todos.txt"

def get_todos(filename = FILENAME):
    """ This is a function
    This reads the file line by line
    And returns as a list """
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filename=FILENAME):
    """This is another function
    This is to overwrite the content of the file
    It needs to be called with a list argument """
    with open(filename, 'w') as file_local:
        todos_local = file_local.writelines(todos_arg)
        

if __name__ == "__main__":
    print("Hello")
    print("This is functions.py!")