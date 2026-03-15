# 2026-03-15
# https://www.acmicpc.net/problem/2573
# bfs

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    ices = set()
    for row in range(N):
        for col in range(M):
            if arr[row][col] > 0:
                ices.add((row, col))

    ans = 0
    while True:
        check = [[0] * M for _ in  range(N)]
        cnt = 0
        for srow in range(N):
            for scol in range(M):
                if not check[srow][scol] and arr[srow][scol] > 0:
                    cnt += 1
                    check[srow][scol] = 1
                    queue = [[srow, scol]]
                    while queue:
                        row, col = queue.pop()
                        for d in range(4):
                            nrow, ncol = row + drow[d], col + dcol[d]
                            if inside(nrow, ncol) and not check[nrow][ncol] and arr[nrow][ncol] > 0:
                                check[nrow][ncol] = 1
                                queue.append([nrow, ncol])

        if cnt >= 2:
            return ans
        if cnt == 0:
            return 0

        melt = [[0] * M for _ in range(N)]
        for row in range(N):
            for col in range(M):
                if arr[row][col] > 0:
                    water = 0
                    for d in range(4):
                        nrow = row + drow[d]
                        ncol = col + dcol[d]

                        if arr[nrow][ncol] == 0:
                            water += 1
                    melt[row][col] = water

        for row in range(N):
            for col in range(M):
                if arr[row][col] > 0:
                    arr[row][col] = max(0, arr[row][col] - melt[row][col])

        ans += 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, arr))