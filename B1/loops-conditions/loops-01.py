# write 100 even numbers using loop in python.
output = []
n = 1
x = 0
while( x < 200 ):
	#x = x+1  
	x += 1
	if x % 2 == 0:
		# print(x)
		output.append(x)
#print(output)
output2 = []
for a in range(200):
	if a % 2 == 0:
		#print(a)
		output2.append(a)
#print(output2)
b = list(range(1,200+1))

print(b, type(b))
output3 = []

for each_val in b:
	if each_val % 2 == 0:
		output3.append(each_val)

print(output3)

r1 = range(0,200, 2)
c = list( r1 )
print("- printing c -")
print(c)
print(  type(r1), type(c) )
#t = list(54231)
#print(t)
#for each_v1 in 4324324:
#	print(5000)


