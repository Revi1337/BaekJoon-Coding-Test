# 2026-03-15
# https://www.acmicpc.net/problem/7569
# bfs

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, L, R, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    ans = 0
    while True:
        check = [[0] * N for _ in range(N)]
        grps = []
        for srow in range(N):
            for scol in range(N):
                if not check[srow][scol]:
                    grp = [[srow, scol]]
                    check[srow][scol] = 1
                    queue = deque([[srow, scol]])
                    while queue:
                        row, col = queue.popleft()
                        for d in range(4):
                            nrow, ncol = row + drow[d], col + dcol[d]
                            if inside(nrow, ncol) and not check[nrow][ncol] and L <= abs(arr[nrow][ncol] - arr[row][col]) <= R:
                                grp.append([nrow, ncol])
                                check[nrow][ncol] = 1
                                queue.append([nrow, ncol])
                    if len(grp) > 1:
                        grps.append(grp)

        if not grps:
            return ans

        ans += 1
        for grp in grps:
            cnt, sm = len(grp), sum([arr[row][col] for row, col in grp])
            nxt = sm // cnt
            for row, col in grp:
                arr[row][col] = nxt

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, L, R, arr))
