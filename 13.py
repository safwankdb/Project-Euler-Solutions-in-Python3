f=open('13.txt','r')
print(str(sum([int(i.strip()) for i in f.read().rsplit('\n')]))[:10])