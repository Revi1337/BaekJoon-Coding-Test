# 2026-04-21
# https://www.acmicpc.net/problem/4485
# 녹색 옷 입은 애가 젤다지?
# V1. bfs(중복 방문을 허용한)
# -> dist 갱신되면 무조건 push
# -> 순서가 중요하지 않음.
# -> queue 는 그냥 작업 리스트 ㅇㅇ
# == 언제든 재처리하는 DP relaxation

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(seq, N, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    INF = 9 * N * N
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = arr[0][0]
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

    return f'Problem {seq}: {dist[N - 1][N - 1]}'

seq = 1
while True:
    N = int(input())
    if not N:
        break
    arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
    print(solution(seq, N, arr))
    seq += 1
