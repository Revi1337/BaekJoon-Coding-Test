import sys

input = sys.stdin.readline

"""
N 과 M (4) (https://www.acmicpc.net/problem/15652)
2024-09-18
"""

def solution(N, M):

    def recursive(depth, number, lst):
        if depth == M:
            answer.append(lst)
            return
        for num in range(number, N + 1):
            recursive(depth + 1, num, lst + [num])

    answer = []
    recursive(0, 1, [])
    for line in answer:
        print(*line)


N, M = map(int, input().split())
solution(N, M)