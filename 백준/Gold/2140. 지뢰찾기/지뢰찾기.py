drow = [-1, -1, 0, 1, 1, 1, 0, -1]
dcol = [0, 1, 1, 1, 0, -1, -1, -1]

def solution(N, board):
    poss, internal = set(), set()
    for row in range(N):
        for col in range(N):
            if row == 0 or row == N - 1 or col == 0 or col == N - 1:
                board[row][col] = int(board[row][col])
                for d in range(8):
                    nrow, ncol = row + drow[d], col + dcol[d]
                    if 0 <= nrow < N and 0 <= ncol < N and board[nrow][ncol] == '#':
                        poss.add((nrow, ncol))
            else:
                internal.add((row, col))

    answer = len(internal - poss)
    poss = sorted(poss, key = lambda x: (x[0], x[1]))
    for row, col in poss:
        can, pos = True, []
        for d in range(8):
            nrow, ncol = row + drow[d], col + dcol[d]
            if board[nrow][ncol] != '#':
                if board[nrow][ncol] == 0:
                    can = False
                else:
                    pos.append((nrow, ncol))
        if can and pos:
            answer += 1
            for r, c in pos:
                board[r][c] = max(0, board[r][c] - 1)

    return answer

N = int(input())
board = [list(input().strip()) for _ in range(N)]
print(solution(N, board))