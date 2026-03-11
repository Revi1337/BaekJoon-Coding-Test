# 2026-03-11
# https://www.acmicpc.net/problem/2559
# psum

def solution(N, K, T):
    psum = [0] * (N + 1)
    for idx in range(1, N + 1):
        psum[idx] = psum[idx - 1] + T[idx - 1]

    return max(psum[st] - psum[st - K] for st in range(K, N + 1))

N, K = map(int, input().split())
T = list(map(int, input().split()))
print(solution(N, K, T))