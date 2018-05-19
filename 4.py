a,k=[],0
for i in range(800,1000):
	for j in range(i,1000):
			a.append(i*j)
for i in a:
	if(str(i)==str(i)[::-1]):
		k=max(i,k)
print(k)