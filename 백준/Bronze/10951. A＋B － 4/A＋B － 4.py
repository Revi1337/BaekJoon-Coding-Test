import sys
while True:
    try:
        f, t = map(int, sys.stdin.readline().rstrip().split())
        print(f + t)
    except Exception as e:
        break