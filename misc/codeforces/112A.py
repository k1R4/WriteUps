l = [str(input()).lower() for i in range(2)]
if l[0] == l[1]:
	print(0)
	exit()
p=[i for i in l]
l.sort()
if l[0] == p[0]:
	print(-1)
else:
	print(1)