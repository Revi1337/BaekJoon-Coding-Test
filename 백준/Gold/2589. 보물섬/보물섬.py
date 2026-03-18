# 2026-03-18
# https://www.acmicpc.net/problem/2589
# bfs

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(L, W, arr):

    inside = lambda row, col: 0 <= row < L and 0 <= col < W

    ans = 0
    for row in range(L):
        for col in range(W):
            if arr[row][col] == 'L':
                check = [[0] * W for _ in range(L)]
                check[row][col] = 1
                queue = deque([(row, col)])
                dist = None
                while queue:
                    srow, scol = queue.popleft()
                    dist = check[srow][scol]
                    for d in range(4):
                        nrow, ncol = srow + drow[d], scol + dcol[d]
                        if inside(nrow, ncol) and not check[nrow][ncol] and arr[nrow][ncol] == 'L':
                            check[nrow][ncol] = check[srow][scol] + 1
                            queue.append((nrow, ncol))

                ans = max(ans, dist - 1)

    return ans

L, W = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(L)]
print(solution(L, W, arr))