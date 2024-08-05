import sys

input = sys.stdin.readline

'''
요다 (https://www.acmicpc.net/problem/5363)
'''

def solution(lines):
    for idx in range(len(lines)):
        line = lines[idx]
        if len(line) > 2:
            line.append(line.pop(0))
            line.append(line.pop(0))
        print(*line, sep=' ')

T = int(input())
lines = [input().split() for _ in range(T)]
solution(lines)