import sys

input = sys.stdin.readline

"""
N 과 M (7) (https://www.acmicpc.net/problem/15656)
2024-09-19
"""

def solution(N, M, numbers):

    numbers.sort()

    def recursive(depth, lst):
        if depth == M:
            answer.append(lst)
            return
        for idx in range(N):
            recursive(depth + 1, lst + [numbers[idx]])

    answer = []
    recursive(0, [])
    for line in answer:
        print(*line)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
solution(N, M, numbers)


