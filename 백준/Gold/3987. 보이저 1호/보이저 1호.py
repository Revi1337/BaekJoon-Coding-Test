drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
dd = {'/': {0: 1, 1: 0, 2: 3, 3: 2}, "\\": {0: 3, 1: 2, 2: 1, 3: 0}}
dmap = ['U', 'R', 'D', 'L']

def solution(N, M, board, PR, PC):

    LIMIT = N * M * 2

    inside = lambda row, col: 0 <= row < N and 0 <= col < M
    end = lambda row, col: not inside(row, col) or board[row][col] == 'C'

    ans = []
    for dir in 0, 1, 2, 3:
        crow, ccol, cnt, d = PR - 1, PC - 1, 1, dir
        ooi = False
        while True:
            nrow, ncol = crow + drow[d], ccol + dcol[d]
            if end(nrow, ncol):
                break
            if board[nrow][ncol] in dd:
                d = dd[board[nrow][ncol]][d]
            crow, ccol, cnt = nrow, ncol, cnt + 1
            if cnt >= LIMIT:
                ooi = True
                break
        ans.append([LIMIT if ooi else cnt, dir])

    ans.sort(key = lambda x: (-x[0], x[1]))
    print(dmap[ans[0][1]], 'Voyager' if ans[0][0] == LIMIT else ans[0][0], sep = '\n')

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
PR, PC = map(int, input().split())
solution(N, M, board, PR, PC)