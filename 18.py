x = []
x.append('75')
x.append('95 64')
x.append('17 47 82')
x.append('18 35 87 10')
x.append('20 04 82 47 65')
x.append('19 01 23 75 03 34')
x.append('88 02 77 73 07 63 67')
x.append('99 65 04 28 06 16 70 92')
x.append('41 41 26 56 83 40 80 70 33')
x.append('41 48 72 33 47 32 37 16 94 29')
x.append('53 71 44 65 25 43 91 52 97 51 14')
x.append('70 11 33 28 77 73 17 78 39 68 17 57')
x.append('91 71 52 38 17 14 91 43 58 50 27 29 48')
x.append('63 66 04 68 89 53 67 30 73 16 69 87 40 31')
x.append('04 62 98 27 23 09 70 98 73 93 38 53 60 04 23')

y = []
for i in x:
    y.append([int(j) for j in i.split()])
n = len(x)
for i in range(n-2, -1, -1):
    row = y[i]
    for j in range(len(row)):
        y[i][j] += max(y[i+1][j], y[i+1][j+1])
print(y)
