import sys

input = sys.stdin.readline

m = int(input().rstrip())
book = 0b0

for _ in range(m):
    oper = input().rstrip().split()
    if oper[0] == 'all':
        book = 0b111111111111111111111
        continue
    if oper[0] == 'empty':
        book = 0b0
        continue

    num = int(oper[1])
    if oper[0] == 'add':
        book = book | (0b1 << num)
    elif oper[0] == 'remove':
        book = book & ~(0b1 << num)
    elif oper[0] == 'check':
        if book & (0b1 << num):
            print(1)
        else:
            print(0)
    elif oper[0] == 'toggle':
        book = book ^ (0b1 << num)

