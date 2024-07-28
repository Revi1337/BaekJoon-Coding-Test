import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, board):
    answer = 0
    ans = 0
    for row in range(N):
        for col in range(M):
            if board[row][col]:
                answer += 1
                board[row][col] = 0
                queue = deque([(row, col)])
                pre = 1
                while queue:
                    r, c = queue.popleft()
                    for d in range(4):
                        nr = r + drow[d]
                        nc = c + dcol[d]
                        if (0 <= nr < N) and (0 <= nc < M) and (board[nr][nc] == 1):
                            pre += 1
                            board[nr][nc] = 0
                            queue.append((nr, nc))
                ans = max(ans, pre)
    print(answer)
    print(ans)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
solution(N, M, board)