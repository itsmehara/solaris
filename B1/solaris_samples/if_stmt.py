
x = 1 # int(input("enter the number"))

if x % 3 == 0:
    print("given is divisible by 3")

if x % 9 == 0:
    print("given is divisible by 9")
else:
    print("given is not divisible by 9")

if x % 12 == 0:
    print("given is divisible by 12")

t1 = (1,2,3,"hello", "a", 5000.23, "4/2/2020")
l1 = [1,2,3,"hello", "a", 5000.23, "4/2/2020"]

import sys

print(sys.getsizeof(t1), sys.getsizeof(l1))
