# 2026-03-11
# https://www.acmicpc.net/problem/1654
# binary_search

def solution(K, N, arr):
    left, right = 1, max(arr) + 1
    while left < right:
        mid = (left + right) // 2
        poss = sum(v // mid for v in arr)
        if poss >= N:
            left = mid + 1
        else:
            right = mid

    return left - 1

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
print(solution(K, N, arr))

