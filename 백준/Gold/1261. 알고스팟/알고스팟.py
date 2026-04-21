# 2026-04-21
# https://www.acmicpc.net/problem/1261
# 알고스팟
# V1. bfs(중복 방문을 허용한)
# -> dist 갱신되면 무조건 push
# -> 순서가 중요하지 않음.
# -> queue 는 그냥 작업 리스트 ㅇㅇ
# == 언제든 재처리하는 DP relaxation

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    INF = N * M
    dist = [[INF] * M for _ in range(N)]
    dist[0][0] = 0
    queue = deque([(0, 0)])

    while queue:
        row, col = queue.popleft()
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if inside(nrow, ncol):
                nc = arr[nrow][ncol]
                if dist[row][col] + nc < dist[nrow][ncol]:
                    dist[nrow][ncol] = dist[row][col] + nc
                    queue.append((nrow, ncol))

    return dist[N - 1][M - 1]

M, N = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
print(solution(N, M, arr))
