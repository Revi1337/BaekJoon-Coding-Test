import sys

input = sys.stdin.readline

"""
N 과 M (2) (https://www.acmicpc.net/problem/15650) 
2024-09-14
"""

def solution(N, M):
    def recursive(level, lst):
        if level == M:
            possible = True
            for idx in range(1, M):
                if lst[idx - 1] >= lst[idx]:
                    possible = False
                    break
            if possible:
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