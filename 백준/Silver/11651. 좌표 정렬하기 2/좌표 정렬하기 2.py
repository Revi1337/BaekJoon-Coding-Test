import sys

def solution(postions):
    positions = sorted(postions, key=lambda x: (x[1], x[0]))
    for x, y in positions:
        print(x, y)

loop = int(sys.stdin.readline())
positions = [
    list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(loop)
]
solution(positions)

