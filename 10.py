sum,a,r=0,[True]*2000000,range(2,2000000)
for i in r:
	if a[i]:
		k,sum=2*i,sum+i
		while k<2000000:
			a[k]=False
			k+=i
print(sum)