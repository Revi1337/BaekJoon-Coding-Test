import sys
from collections import deque

input = sys.stdin.readline

"""
안전 영역 (https://www.acmicpc.net/problem/2468)
2024-09-12
"""

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, board):
    maxH = 1
    for line in board:
        maxH = max(maxH, max(line))

    answer = 0
    for h in range(maxH + 1):
        new = [line[:] for line in board]
        for row in range(N):
            for col in range(N):
                if new[row][col] <= h:
                    new[row][col] = -1

        counter = 0
        for row in range(N):
            for col in range(N):
                if new[row][col] not in [-1, -2]:
                    counter += 1
                    new[row][col] = -2
                    queue = deque([(row, col)])
                    while queue:
                        r, c = queue.popleft()
                        for d in range(4):
                            nr, nc = r + drow[d], c + dcol[d]
                            if (0 <= nr < N) and (0 <= nc < N):
                                if new[nr][nc] not in [-1, -2]:
                                    new[nr][nc] = -2
                                    queue.append((nr, nc))
        answer = max(answer, counter)

    return answer

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))
