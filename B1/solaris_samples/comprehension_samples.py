
t1 = ()
t2 = (1,2,3,"rajesh", "kushal")
print(type(t1))
print(t1)
print()
print(t2)
print(type(t2))
print("--"*20)

l1 = list()
l1.insert(0, 100)
l1.insert(4, 104)
l1.append(300)
l1.insert(0, 105)
l1.insert(0, 106)
print(l1, "--->" ,type(l1))
l1[2] = 333
l1.insert(0, 111)
l1[2] = 44
print(l1)

popped = l1.pop()
print(popped)
print(l1)

popped = l1.pop(3)
print(popped)
print(l1)

l1.insert(3, 111)
l1.insert(2, 111)
l1.insert(0, 111)
print(l1)

l1.remove(44)
print(l1)

print(dir(popped))
print(dir(l1))

l2 = [2,3,11]
l1.append(100)
print(l1)
l1.extend(l2)
print(l1)

print("--"*20)

d1 = {}
d2 = dict()
d3 = {1: 100, 2: 200, 3: "hello"}

print(dir(d3))

d3["a"] = 500
print(d3)

d1["a"] = 500
print(d1)

print(d3[3])
print(d3.get(100))

print("--"*20)
print("- Comprehension -")

# create list with elements below 30 and not div by 5.
# normal way
ll1 = []
for i in range(30):
    if i % 5 != 0:
        ll1.append(i)
print(ll1)

lc2 = [i for i in range(30)  if i%5 != 0]
print(lc2)

# create list with cube elements below 15.

lc3 = [i**3 for i in range(15)]
print(lc3)

print("- dict Comprehension -")


# create dictionary with 3*x-square for each x below 10.

di1 = {}
for i in range(10):
    di1[i] = 3*i*i
print(di1)

di2 = {x: 3*x*x for x in range(10)}
print(di2)