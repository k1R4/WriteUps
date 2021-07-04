n = int(input())
a = [int(i) for i in input().split()]
a.sort()
t,m = sum(a),0
for i in range(n):
	if m<=t:
		p = a.pop()
		m += p
		t -= p
	else:
		break
print(n-len(a))