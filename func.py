FILEPATH = 'todos.txt'

def get_todos(filename=FILEPATH):
    with open(filename, 'r') as file1:
        todos123 = file1.readlines()
    return todos123


def write_todos(todos_arg, filename=FILEPATH):
    with open(filename, 'w') as file2:
        file2.writelines(todos_arg)
