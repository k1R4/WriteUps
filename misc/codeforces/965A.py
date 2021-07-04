from math import ceil
k,n,s,p = [int(i) for i in input().split()]
t=ceil(ceil(n/s)*k/p)
print(t)