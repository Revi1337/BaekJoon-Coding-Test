import sys
while True:
    f, t = map(int, sys.stdin.readline().rstrip().split())
    if f == 0 and t == 0:
        break
    print(f + t)