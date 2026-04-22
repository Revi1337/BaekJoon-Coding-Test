# 2026-04-22
# https://www.acmicpc.net/problem/2665
# 미로 만들기
# V3. bfs(0-1 (heap 없이 다익스트라를 선형화. appendLeft 와 append 로 heap 흉내))

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    INF = N * N
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0
    queue = deque([(dist[0][0], 0, 0)])
    while queue:
        cost, row, col = queue.popleft()
        if cost > dist[row][col]:
            continue
        if row == col == N - 1:
            return dist[N - 1][N - 1]
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if inside(nrow, ncol):
                if arr[nrow][ncol] and dist[row][col] < dist[nrow][ncol]:
                    dist[nrow][ncol] = dist[row][col]
                    queue.appendleft((dist[nrow][ncol], nrow, ncol))
                elif not arr[nrow][ncol] and dist[row][col] + 1 < dist[nrow][ncol]:
                    dist[nrow][ncol] = dist[row][col] + 1
                    queue.append((dist[nrow][ncol], nrow, ncol))

    return None # Impossible

N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
print(solution(N, arr))