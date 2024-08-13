import sys
from collections import deque

input = sys.stdin.readline

def solution(N, bals):
    bals = deque(enumerate(bals, start=1))
    answer = []
    while bals:
        idx, paper = bals.popleft()
        answer.append(idx)
        if paper > 0:
            bals.rotate(-(paper - 1))
        elif paper < 0:
            bals.rotate(-paper)

    print(*answer, sep = ' ')

N = int(input())
bals = list(map(int, input().split()))
solution(N, bals)
