drow = [0, -1, 0, 1]
dcol = [-1, 0, 1, 0]

def solution(N, M, K, board):
    answer, srow, scol, d = 0, 0, 0, 2
    back, top, left, right, front, bottom = 2, 1, 4, 3, 5, 6

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    for _ in range(K):
        nrow, ncol = srow + drow[d], scol + dcol[d]
        if inside(nrow, ncol):
            srow, scol = nrow, ncol
        else:
            d = (d + 2) % 4
            srow, scol = srow + drow[d], scol + dcol[d]

        if d == 0:
            left, top, right, bottom = top, right, bottom, left
        elif d == 1:
            back, top, front, bottom = top, front, bottom, back
        elif d == 2:
            left, top, right, bottom = bottom, left, top, right
        else:
            back, top, front, bottom = bottom, back, top, front

        B, C = board[srow][scol], 1
        queue = [[srow, scol]]
        check = [[0] * M for _ in range(N)]
        check[srow][scol] = 1
        while queue:
            row, col = queue.pop()
            for dir in range(4):
                nrow, ncol = row + drow[dir], col + dcol[dir]
                if not inside(nrow, ncol) or check[nrow][ncol] or board[nrow][ncol] != B:
                    continue
                check[nrow][ncol] = 1
                queue.append([nrow, ncol])
                C += 1
        answer += B * C

        A = bottom
        if A > B:
            d = (d + 1) % 4
        elif A < B:
            d = (d - 1) % 4

    return answer

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, K, board))