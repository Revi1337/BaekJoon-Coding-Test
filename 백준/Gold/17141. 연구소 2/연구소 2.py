# 2025-10-01
# https://www.acmicpc.net/problem/17141

import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, arr):

    INF = float('inf')
    inside = lambda row, col : 0 <= row < N and 0 <= col < N

    def spread(active):
        queue, check = deque(), [[-1] * N for _ in range(N)]
        for row, col in active:
            queue.append((row, col))
            check[row][col] = 0

        fill = mx = 0
        while queue:
            row, col = queue.popleft()
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if not inside(nrow, ncol):
                    continue
                if arr[nrow][ncol] != 1 and check[nrow][ncol] == -1:
                    check[nrow][ncol] = check[row][col] + 1
                    fill, mx = fill + 1, check[nrow][ncol]
                    queue.append((nrow, ncol))

        return mx if fill == ecnt else INF

    def backtrack(lst, st):
        if len(lst) == M:
            nonlocal ans
            ans = min(ans, spread(lst))
            return

        for idx in range(st, len(virus)):
            lst.append(virus[idx])
            backtrack(lst, idx + 1)
            lst.pop()

    ecnt, virus = 0, []
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                virus.append((row, col))
            elif arr[row][col] == 0:
                ecnt += 1
    ecnt += len(virus) - M
    if not ecnt:
        return 0

    ans = INF
    backtrack([], 0)

    return ans if ans != INF else -1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, arr))

