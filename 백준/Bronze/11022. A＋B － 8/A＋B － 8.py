import sys
loop = int(input())
for i in range(loop):
    f, t = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{i + 1}: {f} + {t} = {f + t}")