import sys

input = sys.stdin.readline

"""
N 과 M (6) (https://www.acmicpc.net/problem/15655)
2024-09-18
"""

def solution(N, M, numbers):

    numbers.sort()

    def recursive(depth, index, lst):
        if depth == M:
            answer.append(lst)
            return
        for idx in range(index, N):
            if not check[idx] and idx >= index:
                check[idx] = 1
                recursive(depth + 1, idx, lst + [numbers[idx]])
                check[idx] = 0

    check = [0] * N
    answer = []
    recursive(0, 0, [])

    for line in answer:
        print(*line)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
solution(N, M, numbers)
