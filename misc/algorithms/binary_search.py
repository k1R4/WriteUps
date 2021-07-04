l = [int(i) for i in input().split()]
x = int(input())

def binary_search(l,x,m,n):
	if l[n//2] == x:
		return n//2
	elif l[n//2] < x:
		return binary_search(l,x,(n//2)+1,n)
	else:
		return binary_search(l,x,m,(n//2)-1)

print(binary_search(l,x,0,len(l)-1))