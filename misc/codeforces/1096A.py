n = int(input())
l = [[int(i) for i in input().split()] for i in range(n)]
for i in range(n):
	print(f"{l[i][0]} {l[i][0]*2}")