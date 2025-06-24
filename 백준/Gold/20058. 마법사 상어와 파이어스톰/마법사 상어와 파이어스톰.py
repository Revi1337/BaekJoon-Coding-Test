from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, Q, board, oper):

    S = 2 ** N
    inside = lambda row, col: 0 <= row < S and 0 <= col < S

    def mx_cluster():
        check = [[0] * S for _ in range(S)]
        mx = 0
        for r in range(S):
            for c in range(S):
                if board[r][c] and not check[r][c]:
                    queue = deque([(r, c)])
                    tmp = check[r][c] = 1
                    while queue:
                        row, col = queue.popleft()
                        for d in range(4):
                            nrow, ncol = row + drow[d], col + dcol[d]
                            if not inside(nrow, ncol):
                                continue
                            if board[nrow][ncol] and not check[nrow][ncol]:
                                queue.append((nrow, ncol))
                                check[nrow][ncol] = 1
                                tmp += 1
                    mx = max(mx, tmp)
        return mx

    def decrease():
        lst = []
        for row in range(S):
            for col in range(S):
                if not board[row][col]:
                    continue
                cnt = 0
                for d in range(4):
                    nrow, ncol = row + drow[d], col + dcol[d]
                    if inside(nrow, ncol) and board[nrow][ncol]:
                        cnt += 1
                if cnt < 3:
                    lst.append([row, col])
        for row, col in lst:
            board[row][col] -= 1

    def rotate(l):
        nboard = [[0] * S for _ in range(S)]
        size = 2 ** l
        for off_row in range(0, S, size):
            for off_col in range(0, S, size):
                for r in range(size):
                    for c in range(size):
                        nboard[off_row + c][off_col + size - 1 - r] = board[off_row + r][off_col + c]

        return nboard

    for l in oper:
        board = rotate(l)
        decrease()

    sm = sum(sum(line) for line in board)
    mx = mx_cluster()

    print(sm, mx, sep = '\n')

N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2 ** N)]
oper = list(map(int, input().split()))
solution(N, Q, board, oper)