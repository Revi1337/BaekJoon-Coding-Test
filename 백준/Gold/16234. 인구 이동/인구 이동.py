from collections import deque
import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, L, R, board):
    answer = 0
    while answer <= 2000:
        queue = deque()
        flag = 0
        check = [[0] * N for _ in range(N)]
        for row in range(N):
            for col in range(N):
                if not check[row][col]:
                    queue.append((row, col))
                    check[row][col] = 1
                    team = [(row, col)]
                    total = board[row][col]
                    while queue:
                        r, c = queue.popleft()
                        for d in range(4):
                            nr = r + drow[d]
                            nc = c + dcol[d]
                            if (0 <= nr < N) and (0 <= nc < N) and (not check[nr][nc]) and (L <= abs(board[r][c] - board[nr][nc]) <= R):
                                queue.append((nr, nc))
                                check[nr][nc] = 1
                                team.append((nr, nc))
                                total += board[nr][nc]
                    if len(team) > 1:
                        for ti, tj in team:
                            board[ti][tj] = total // len(team)
                        flag = 1
        if flag == 0:
            break
        answer += 1
    return answer

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, L, R, board))
