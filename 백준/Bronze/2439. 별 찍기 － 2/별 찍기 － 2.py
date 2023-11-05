loop = int(input())
for i in range(loop):
    blank = loop - (i + 1)
    print(blank * ' ' + '*' * (i + 1))