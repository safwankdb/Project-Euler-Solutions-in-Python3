n=1
while True:
	t,c=int((n*(n+1))/2),1
	for i in range(1,int(t)):
		if n%i==0:
			c+=1
	print(n,t,c)
	if c>500:
		break
	n+=1