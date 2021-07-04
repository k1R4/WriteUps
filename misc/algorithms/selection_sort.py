l = [int(i) for i in input().split()]

for i in range(len(l)):
    k = i
    for j in range(i+1, len(l)):
        if l[k] > l[j]:
            k = j       
    l[i], l[k] = l[k], l[i]

for i in l:
	print(i,end=" ")
print()