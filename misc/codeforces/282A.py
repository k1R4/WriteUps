n = int(input())
c = [input() for i in range(n)]
t=0
for i in c:
	if "+" in i:
		t+=1
	else:
		t-=1
print(t)