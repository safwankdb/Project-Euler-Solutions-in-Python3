n,c=120000,1
a=[True]*(n+1)
for i in range(2,n+1):
	if a[i]:
		k=2*i
		while k<=n:
			a[k]=False
			k+=i
for i in range(2,n+1):
	if a[i]:
		if c==10001:
			print(i)
			break
		c+=1