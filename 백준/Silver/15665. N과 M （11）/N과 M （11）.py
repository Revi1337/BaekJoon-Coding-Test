import sys

input = sys.stdin.readline

"""
N 과 M (11) (https://www.acmicpc.net/problem/15665)
2024-09-26
"""

def solution(N, M, numbers):
    numbers.sort()

    def recursive(depth, lst):
        if depth == M:
            answer.append(lst)
            return
        prev = 0
        for idx in range(N):
            if numbers[idx] != prev:
                prev = numbers[idx]
                recursive(depth + 1, lst + [numbers[idx]])

    answer = []
    recursive(0, [])
    for ans in answer:
        print(*ans)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
solution(N, M, numbers)
