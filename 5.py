r,l=list(range(2,21)),1
def prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True
for i in r:
	if prime(i):
		l*=i
k=l
while True:
	flag=True
	for i in r:
		if k%i!=0:
			k+=l
			flag=False
	if flag:
		break
print(k)