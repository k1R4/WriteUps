par = str(input())
stack = []
opn,clos = ["(","[","{"],[")","]","}"]

for i in par:
	if i in opn:
		stack.append(i)
	elif i in clos:
		if i != clos[opn.index(stack[-1])]:
			print("Unbalanced")
			exit()
		else:
			stack.pop()
print("Balanced")