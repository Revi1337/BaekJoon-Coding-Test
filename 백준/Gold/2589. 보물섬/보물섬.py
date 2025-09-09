import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(L, W, arr):

    LAND, SEA = 'L', 'W'
    inside = lambda row, col : 0 <= row < L and 0 <= col < W

    def find_cluster(srow, scol):
        queue = deque([[srow, scol]])
        check[srow][scol] = 1
        cluster = []
        while queue:
            row, col = queue.popleft()
            cluster.append([row, col])
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if not inside(nrow, ncol) or check[nrow][ncol] or arr[nrow][ncol] == SEA:
                    continue
                check[nrow][ncol] = 1
                queue.append([nrow, ncol])
        return cluster

    def find_dist(srow, scol):
        check = [[0] * W for _ in range(L)]
        mx = check[srow][scol] = 1
        queue = deque([[srow, scol]])
        while queue:
            row, col = queue.popleft()
            mx = max(mx, check[row][col])
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if not inside(nrow, ncol) or check[nrow][ncol] or arr[nrow][ncol] == SEA:
                    continue
                check[nrow][ncol] = check[row][col] + 1
                queue.append([nrow, ncol])
        return mx - 1

    check = [[0] * W for _ in range(L)]
    clusters = []
    for row in range(L):
        for col in range(W):
            if arr[row][col] == LAND and not check[row][col]:
                clusters.append(find_cluster(row, col))

    ans = 0
    for cluster in clusters:
        for row, col in cluster:
            ans = max(ans, find_dist(row, col))

    return ans

L, W = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(L)]
print(solution(L, W, arr))