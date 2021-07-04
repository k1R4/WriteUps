n = int(input())
h,l = "I hate ","I love "
t = False
o = ""
for i in range(n):
	if t:
		o += l+"that "
		t = False
	else:
		o += h+"that "
		t = True
print(o.rstrip("that ")+" it")