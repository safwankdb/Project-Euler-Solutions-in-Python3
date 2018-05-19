Collatz,c=dict(),0
Collatz[1]=1
def collatz(n):
	if n in Collatz:
		return Collatz[n]
	Collatz[n]=1+collatz((n%2)*(3*n+1)+(1-(n%2))*n/2)
	return Collatz[n]
for n in range(1,1000000):
	print(n,collatz(n))
	if collatz(n)>c:
		m=n
		c=collatz(n)
print(m,c)