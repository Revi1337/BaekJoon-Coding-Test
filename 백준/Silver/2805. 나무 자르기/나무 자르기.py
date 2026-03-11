# 2026-03-11
# https://www.acmicpc.net/problem/2805
# binary_search

def solution(N, M, H):
    left, right = 0, max(H) + 1
    while left < right:
        mid = (left + right) // 2
        poss = sum(h - mid for h in H if h > mid)
        if poss >= M:
            left = mid + 1
        else:
            right = mid

    return left - 1

N, M = map(int, input().split())
H = list(map(int, input().split()))
print(solution(N, M, H))