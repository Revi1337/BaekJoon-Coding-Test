drow = [-1, -1, 0, 1, 1, 1, 0, -1]
dcol = [0, 1, 1, 1, 0, -1, -1, -1]

def solution(N, M, positions):
    board = [[0] * (N + 1) for _ in range(N + 1)]
    mid = N // 2
    board[mid][mid] = board[mid + 1][mid + 1] = 2
    board[mid + 1][mid] = board[mid][mid + 1] = 1

    for (col, row, rock) in positions:
        board[col][row] = rock
        for d in range(8):
            r = []
            for mul in range(1, N):
                ncol, nrow = col + dcol[d] * mul , row + drow[d] * mul
                if (1 <= ncol <= N) and (1 <= nrow <= N):
                    if board[ncol][nrow] == 0:
                        break
                    elif board[ncol][nrow] == rock:
                        while r:
                            tcol, trow = r.pop()
                            board[tcol][trow] = rock
                        break
                    else:
                        r.append((ncol, nrow))
                else:
                    break

    bcnt = wcnt = 0
    for rocks in board:
        bcnt += rocks.count(1)
        wcnt += rocks.count(2)

    return f'{bcnt} {wcnt}'

T = int(input())
for index in range(T):
    N, M = map(int, input().split())
    positions = [list(map(int, input().split())) for _ in range(M)]
    print(f'#{index + 1} {solution(N, M, positions)}')