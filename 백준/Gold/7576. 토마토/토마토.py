import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(M, N, box):
    queue = deque()
    distance = [[0] * M for _ in range(N)]
    answer = -1e9
    for row in range(N):
        for col in range(M):
            if box[row][col] == 1:
                distance[row][col] = 1
                queue.append((row, col))

    while queue:
        row, col = queue.popleft()
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < N) and (0 <= ncol < M) and (box[nrow][ncol] == 0) and (distance[nrow][ncol] == 0):
                distance[nrow][ncol] = distance[row][col] + 1
                queue.append((nrow, ncol))

    for row in range(N):
        for col in range(M):
            if distance[row][col] == 0 and box[row][col] != -1:
                return -1
            answer = max(answer, distance[row][col])

    return answer - 1

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
print(solution(M, N, box))