l = [int(i) for i in input().split()]

for i in range(len(l)):
	for j in range(len(l)-i-1):
		if l[j] > l[j+1]:
			l[j], l[j+1] = l[j+1], l[j]

for i in l:
	print(i,end=" ")
print()