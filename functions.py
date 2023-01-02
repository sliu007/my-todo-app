FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list
    of to-do items.
    """
    with open(filepath, "r") as tl:
        tl = tl.readlines()
        return tl

#print(help(get_todos()))

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file.
    """
    with open(filepath, "w") as tl:
        tl.writelines(todos_arg)

#print(help(write_todos()))


if __name__ == "__main__":
    print("Hello")
    print(get_todos())