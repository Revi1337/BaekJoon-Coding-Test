# 2026-03-11
# https://www.acmicpc.net/problem/11660
# 2d arr psum

def solution(N, M, arr, T):
    psum = [[0] * (N + 1) for _ in range(N + 1)]
    for idx in range(1, N + 1):
        for jdx in range(1, N + 1):
            psum[idx][jdx] = psum[idx - 1][jdx] + psum[idx][jdx - 1] - psum[idx - 1][jdx - 1] + arr[idx - 1][jdx - 1]

    for r1, c1, r2, c2 in T:
        sm = psum[r2][c2] - psum[r1 - 1][c2] - psum[r2][c1 - 1] + psum[r1 - 1][c1 - 1]
        print(sm)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
T = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, arr, T)

