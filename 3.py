import math
r=range(2,math.ceil(600851475143**(0.5)))
b=[True]*(len(r)+2)
for i in r:
	if(b[i]):
		k=2*i
	while(k<len(b)):
			b[k]=False
			k+=i
for i in r:
	if(b[i]):
		if(600851475143%i==0):
			a=i
print(a)