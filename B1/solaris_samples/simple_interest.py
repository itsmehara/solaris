print("write a program to caliculate simple interest.")
# use functions

def simple_interest(name, principle=5000, _time=1, rate=2):
    si = (principle *_time * 12 * rate) / 100
    print("total interest is :", si, "for customer:", name)
    return si

val1 = simple_interest("hara",10000, 2, 1.5)
print(val1)
val2 = simple_interest("rajesh")
print(val2)
