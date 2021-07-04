from math import ceil
n,m,a = [int(i) for i in input().split()]
b,h = ceil(m/a),ceil(n/a)
print(b*h)