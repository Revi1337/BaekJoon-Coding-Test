# 2026-03-12
# https://www.acmicpc.net/problem/2512
# binary_search

import sys

input = sys.stdin.readline

"""upper bound (1)"""
def solution(N, arr, M):
    left, right = 0, max(arr) + 1
    while left < right:
        mid = (left + right) // 2
        sm = sum(min(v, mid) for v in arr)
        if sm <= M:
            left = mid + 1
        else:
            right = mid

    return left - 1

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
print(solution(N, arr, M))

