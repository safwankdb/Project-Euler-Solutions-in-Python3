fib=dict()
fib[1]=1
fib[2]=2
def fibonacci(n):
	if n in fib:
		return fib[n]
	else:
		fib[n] = fibonacci(n-2)+fibonacci(n-1)
		return fib[n]
k=0
sum=0
while fibonacci(3*k+2) <= 4000000:
	print(fib[3*k+2])
	sum+=fib[3*k+2]
	k+=1
print(sum)