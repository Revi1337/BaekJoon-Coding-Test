import sys

input = sys.stdin.readline

def solution(N, M, T):
    T.sort()
    left, right = T[0], T[-1] * M + 1
    while left < right:
        mid = (left + right) // 2
        cnt = sum(mid // t for t in T)
        if cnt >= M:
            right = mid
        else:
            left = mid + 1

    return right

N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]
print(solution(N, M, T))