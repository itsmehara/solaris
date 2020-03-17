
def read_data():
    with open("funcs.py") as fhandle:
        for line in fhandle.readlines():
            print(line)

read_data()