
#defining a function with variable number of arguements
def add_given(*args):
    sumx = 0
    for val in args:
        sumx = sumx + val
        #print(val)
    return sumx

val1 = add_given(1,2,3,4,5,6)
print(val1)

val = add_given()
print(val)