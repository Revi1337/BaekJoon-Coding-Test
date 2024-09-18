import sys

input = sys.stdin.readline

"""
N 과 M (5) (https://www.acmicpc.net/problem/15654)
2024-09-18
"""

def solution(N, M, numbers):
    numbers.sort()

    def recursive(depth, lst):
        if depth == M:
            answer.append(lst)
            return
        for idx in range(N):
            if not check[idx]:
                check[idx] = 1
                recursive(depth + 1, lst + [numbers[idx]])
                check[idx] = 0

    answer = []
    check = [0] * N
    recursive(0, [])
    for line in answer:
        print(*line)


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
solution(N, M, numbers)
