# 2025-09-18
# https://www.acmicpc.net/problem/1913

import sys

input = sys.stdin.readline

# 하, 우, 상, 좌
drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    arr = [[0] * N for _ in range(N)]
    srow = scol = d = 0
    st = N ** 2
    arr[srow][scol] = st
    st -= 1

    ans = [1, 1]
    while st > 0:
        nrow, ncol = srow + drow[d], scol + dcol[d]
        if not inside(nrow, ncol) or arr[nrow][ncol]:
            d = (d + 1) % 4
        else:
            arr[nrow][ncol] = st
            srow, scol = nrow, ncol
            if st == M:
                ans = [srow + 1, scol + 1]
            st -= 1

    for line in arr:
        print(*line)
    print(*ans)

N = int(input())
M = int(input())
solution(N, M)