# 2025-10-01
# https://www.acmicpc.net/problem/1937

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, arr):

    inside = lambda row, col : 0 <= row < N and 0 <= col < N

    def recursive(srow, scol):
        if memo[srow][scol]:
            return memo[srow][scol]

        mx = 1
        for d in range(4):
            nrow, ncol = srow + drow[d], scol + dcol[d]
            if not inside(nrow, ncol):
                continue
            if arr[srow][scol] < arr[nrow][ncol]:
                mx = max(mx, 1 + recursive(nrow, ncol))

        memo[srow][scol] = mx
        return memo[srow][scol]

    memo = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if not memo[row][col]:
                recursive(row, col)

    return max(max(line) for line in memo)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))
