import sys

input = sys.stdin.readline

"""
N 과 M (9) (https://www.acmicpc.net/problem/15663)
2024-09-25
"""

def solution(N, M, numbers):
    numbers.sort()
    def recursive(depth, lst):
        if depth == M:
            answer.append(lst)
            return
        prev = 0
        for idx in range(N):
            if not check[idx] and prev != numbers[idx]:
                prev = numbers[idx]
                check[idx] = 1
                recursive(depth + 1, lst + [numbers[idx]])
                check[idx] = 0

    answer = []
    check = [0] * N
    recursive(0, [])
    for ans in answer:
        print(*ans)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
solution(N, M, numbers)
