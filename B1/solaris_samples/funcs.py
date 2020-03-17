def do_some_oppr():
    print("some activity done.")

def add_given(a,b):
    sum_of_given = a+b
    return sum_of_given

def add_three(a,b,c=100):
    sum_of_given = a+b+c
    return sum_of_given

add_given(100,4400)

val = add_given(100,4400)
print(val)
val2 = add_three(100,4400, 232)
print(val2)
val3 = do_some_oppr()
print(val3)
val4 = add_three(100,4400)
print(val4)