l = [str(input()) for i in range(5)]
x,y = 0,0
for i in range(5):
	if "1" in l[i]:
		y = i+1
		for j in range(5):
			if l[i].split()[j] == "1":
				x = j+1
				break
		break
print(abs(3-x)+abs(3-y))