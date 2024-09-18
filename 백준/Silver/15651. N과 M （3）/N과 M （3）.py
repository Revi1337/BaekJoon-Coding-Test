import sys

input = sys.stdin.readline

"""
N 과 M (3) (https://www.acmicpc.net/problem/15651)
2024-09-18
"""

def solution(N, M):

    def recursive(depth, lst):
        if depth == M:
            answer.append(lst)
            return
        for number in range(1, N + 1):
            recursive(depth + 1, lst + [number])

    answer = []
    recursive(0, [])
    for line in answer:
        print(*line)


N, M = map(int, input().split())
solution(N, M)