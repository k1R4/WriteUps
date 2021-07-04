n = int(input())
w = [input() for i in range(n)]

for i in range(n):
	l = len(w[i])
	if l>10:
		print(f"{w[i][0]}{l-2}{w[i][l-1]}")
	else:
		print(w[i])