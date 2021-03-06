# ToDo-app
import os.path


def OpenFile(f):
    """Reads file specified in parameter, and returns a list with it's rows"""
    if not os.path.isfile(f):
        open(f, "w").close()
    db_file = open(f, "r")
    d = {}
    for line in db_file:
        splitted = line.strip().split(sep=',')
        if splitted[0] == 'x':
            d[splitted[1]] = True
        elif splitted[0] == '_':
            d[splitted[1]] = False
    db_file.close()
    return d


def WriteFile(f, d):
    db_file = open(f, "w")
    for line in d:
        if d[line]:
            db_file.write("x," + line + "\n")
        elif not d[line]:
            db_file.write("_," + line + "\n")
    db_file.close()


def AddItem(d):
    """Adds an item from input to the parameter dictionary with value of False
        and returns the new dict"""
    input_string = input("Add an item: ")
    if input_string not in d:
        d[input_string] = False
        print("Item added")
    else:
        print("Item already in list")
    return d


def ListItems(d):
    print("You saved the following to-do items:")
    for line in d:
        if d[line]:
            print("   ", list(d.keys()).index(line)+1, "[x]", line)
        elif not d[line]:
            print("   ", list(d.keys()).index(line)+1, "[ ]", line)


def MarkItem(d):
    ListItems(d)
    input_int = int(input("Which one you want to mark as completed: "))
    d[list(d.keys())[input_int - 1]] = True
    # print(d[list(d.keys())[input_int - 1]])


def DeleteMarked(d):
    new_d = {}
    for item in d:
        if not d[item]:
            new_d[item] = False
    return new_d


def main():
    run = True
    db = {}
    db_filename = "list.txt"

    db = OpenFile(db_filename)
    while run:
        print()
        input_string = \
            input("Please specify a command [list, add, mark, archive]: ")
        if input_string == "list":
            ListItems(db)
        elif input_string == "add":
            db = AddItem(db)
        elif input_string == "mark":
            MarkItem(db)
        elif input_string == "archive":
            db = DeleteMarked(db)
            print("All completed tasks got deleted.")
        elif input_string == "x":
            WriteFile(db_filename, db)
            run = False

main()
