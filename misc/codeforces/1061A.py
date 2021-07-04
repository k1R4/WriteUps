n,s = [int(i) for i in input().split()]
c = 0
t = 0
while t<s:
	if t+n<=s:
		t += n
		c += 1
	else:
		n -= 1

print(c)