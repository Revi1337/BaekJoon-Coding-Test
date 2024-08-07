import sys

input = sys.stdin.readline

'''
시리얼 번호 (https://www.acmicpc.net/problem/1431)
'''

def solution(N, strings):
    ss = sorted(
        strings,
        key = lambda x: (
            len(x),
            sum(map(lambda v1: int(v1), filter(lambda v: v.isdecimal(), x))),
            x
        )
    )

    print(*ss, sep = '\n')

N = int(input())
strings = [input().strip() for _ in range(N)]
solution(N, strings)
