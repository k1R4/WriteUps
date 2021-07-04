w,h,k = [int(i) for i in input().split()]
n = 0
for i in range(1,k+1):
	n += (h-(4*(i-1)))*(w-(4*(i-1)))
	n -= (h-(4*(i-1))-2)*(w-(4*(i-1))-2)
print(n)