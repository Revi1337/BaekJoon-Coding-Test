# 2026-03-11
# https://www.acmicpc.net/problem/2805
# binary_search

import sys

input = sys.stdin.readline

"""upper bound (2)"""
def solution(N, M, H):
    left, right = 0, max(H) + 1
    while left < right:
        mid = (left + right + 1) // 2
        poss = sum(h - mid for h in H if h > mid)
        if poss >= M:
            left = mid
        else:
            right = mid - 1

    return left

N, M = map(int, input().split())
H = list(map(int, input().split()))
print(solution(N, M, H))