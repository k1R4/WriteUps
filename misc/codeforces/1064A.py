a,b,c = [int(i) for i in input().split()]
t=0
while True:
	if a+b>c:
		if b+c>a:
			if a+c>b:
				break
			else:
				if a<b+c:
					a+=1
					t+=1
				elif c<a+b:
					c+=1
					t+=1
		else:
			if b<a+c:
				b+=1
				t+=1
			elif c<a+b:
				c+=1
				t+=1
	else:
		if a<b+c:
			a+=1
			t+=1
		elif b<a+c:
			b+=1
			t+=1

print(t)