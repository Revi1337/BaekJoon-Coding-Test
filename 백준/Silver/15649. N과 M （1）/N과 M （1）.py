import sys

input = sys.stdin.readline

"""
N 과 M (1) (https://www.acmicpc.net/problem/15649) 
2024-09-14
"""

def solution(N, M):

    def recursive(level, lst):
        if level == M:
            answer.append(lst)
            return
        for idx in range(1, N + 1):
            if not check[idx]:
                check[idx] = 1
                recursive(level + 1, lst + [idx])
                check[idx] = 0

    answer = []
    check = [0] * (N + 1)
    recursive(0, [])
    for line in answer:
        print(*line)

N, M = map(int, input().split())
solution(N, M)