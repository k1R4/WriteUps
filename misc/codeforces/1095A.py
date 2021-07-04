n = int(input())
enc = input()
dec = ""
i,j = 0,0
while j<n:
	dec += enc[j]
	i += 1
	j += i
print(dec)