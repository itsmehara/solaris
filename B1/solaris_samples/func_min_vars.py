# function with minimum two args and variable number of args
def add_vals(a,b=9,*vals):
    sumx = a + b
    #sumx = 0  # a #+ b
    for val in vals:
        sumx = sumx + val
    return sumx
value = add_vals(100,20)
print(value)

value = add_vals(12,14,4,6,213,353,2,3,464)
print(value)

tup1 = (1,532,2,3,5,2,14,4,6,23,53,2,3,44)
#print(sum(tup1))
sumy = add_vals(*tup1)
print(sumy)

