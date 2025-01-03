# 하 우 상 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def solution(N, M, R, board):
    ir = ic = 0
    for _ in range(R):
        for depth in range(min(N, M) // 2):
            sr, sc, d = ir + depth, ic + depth, 0
            r, c = sr, sc
            prev = board[sr][sc]
            while True:
                nr, nc = r + dr[d], c + dc[d]
                if not (depth <= nr < N - depth and depth <= nc < M - depth):
                    d = (d + 1) % 4
                    continue
                board[nr][nc], prev = prev, board[nr][nc]
                r, c = nr, nc
                if (r, c) == (sr, sc):
                    break

    for line in board:
        print(*line)

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
solution(N, M, R, board)
