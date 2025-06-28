def solution(N, M, board):

    dir = [[[0, -1], [1, 0]], [[0, -1], [-1, 0]], [[-1, 0], [0, 1]], [[1, 0], [0, 1]]]

    inside = lambda row, col: 0 <= row < N and 0 <= col < M
    possible = lambda row, col: inside(row, col) and not check[row][col]

    def backtrack(st, sm):
        nonlocal mx
        mx = max(mx, sm)
        for idx in range(st, N * M):
            row, col = idx // M, idx % M
            if check[row][col]:
                continue
            for chunk1, chunk2 in dir:
                (drow1, dcol1), (drow2, dcol2) = chunk1, chunk2
                nrow1, ncol1, nrow2, ncol2 = row + drow1, col + dcol1, row + drow2, col + dcol2
                if possible(nrow1, ncol1) and possible(nrow2, ncol2):
                    check[row][col] = check[nrow1][ncol1] = check[nrow2][ncol2] = 1
                    backtrack(idx + 1, sm + board[row][col] * 2 + board[nrow1][ncol1] + board[nrow2][ncol2])
                    check[row][col] = check[nrow1][ncol1] = check[nrow2][ncol2] = 0

    mx, check = 0, [[0] * M for _ in range(N)]
    backtrack(0, 0)
    return mx

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
