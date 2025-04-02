from collections import deque

drow = [-1, 1, 0, 0, -1, -1, 1, 1]
dcol = [0, 0, -1, 1, -1, 1, -1, 1]

def solution(N, M, board):
    check = [[0] * M for _ in range(N)]
    answer = 0
    for row in range(N):
        for col in range(M):
            if not check[row][col]:
                check[row][col] = 1
                queue = deque([(row, col)])
                edges = set()
                while queue:
                    sr, sc = queue.popleft()
                    for d in range(8):
                        nr, nc = sr + drow[d], sc + dcol[d]
                        if 0 <= nr < N and 0 <= nc < M:
                            if board[nr][nc] != board[sr][sc]:
                                edges.add((nr, nc))
                            else:
                                if not check[nr][nc]:
                                    check[nr][nc] = 1
                                    queue.append((nr, nc))
                for er, ec in edges:
                    if board[er][ec] > board[row][col]:
                        break
                else:
                    answer += 1

    return answer

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
