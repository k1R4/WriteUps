n = int(input())
r = [int(i) for i in input().split()]
for i in range(n):
	if r[i] == 1:
		print("hard")
		exit()
print("easy")