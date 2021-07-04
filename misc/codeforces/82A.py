from math import ceil
n = int(input())
q = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
t = 0
while n>5*(2**t):
	n-=5*(2**t)
	t+=1
if t==0:
	print(q[n-1])
	exit()
print(q[int((n-1)/(2**t))])