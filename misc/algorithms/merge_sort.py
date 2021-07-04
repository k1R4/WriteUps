def merge(a,b):
	merged = []
	m,n = len(a),len(b)
	i,j = 0,0

	while i<m and j<n:
		if a[i] <= b[j]:
			merged.append(a[i])
			i+=1
		else:
			merged.append(b[j])
			j+=1

	for k in range(i,m):
		merged.append(a[k])

	for k in range(j,n):
		merged.append(b[k])

	return merged

def sort(l):
	x = len(l)
	if x == 1:
		return l

	a,b = sort(l[:x//2]),sort(l[x//2:])
	return merge(a,b)

l = [int(i) for i in input().split()]
print(sort(l))