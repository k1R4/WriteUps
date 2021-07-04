n = int(input())
l = [[int(i) for i in input().split()] for i in range(n)]

for i in range(n):
	x = l[i][0]^l[i][1]
	m = l[i][2]%3
	if m == 0:
		print(l[i][0])
	if m == 1:
		print(l[i][1])
	if m == 2:
		print(x)