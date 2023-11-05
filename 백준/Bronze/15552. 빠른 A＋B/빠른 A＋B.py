import sys
loop = int(input())
for _ in range(loop):
    f, t = map(int, sys.stdin.readline().rstrip().split())
    print(f + t)