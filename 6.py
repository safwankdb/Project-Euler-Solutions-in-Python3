sum=0
for i in range(1,101):
	for j in range(1,101):
		if i!=j:
			sum+=i*j
print(sum)