import sys

input = sys.stdin.readline

"""
Binary Search (Parametric Search)
"""
def solution(N, M, T):
    T.sort()
    left, right = T[0], T[-1] * M + 1
    while left < right:
        mid = (left + right) // 2
        cnt = sum(mid // t for t in T)
        if cnt < M:
            left = mid + 1
        else:
            right = mid

    return right

N, M = map(int, input().split())
T = list(map(int, input().split()))
print(solution(N, M, T))