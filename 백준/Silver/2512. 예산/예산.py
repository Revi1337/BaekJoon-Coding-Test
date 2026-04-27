# 2026-03-12
# https://www.acmicpc.net/problem/2512
# binary_search

import sys

input = sys.stdin.readline

def solution(N, arr, M):
    ans, left, right = 0, 0, max(arr)
    while left <= right:
        mid = (left + right) // 2
        sm = sum(min(v, mid) for v in arr)
        if sm <= M:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
print(solution(N, arr, M))

