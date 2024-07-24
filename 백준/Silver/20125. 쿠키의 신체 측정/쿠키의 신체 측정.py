import sys

input = sys.stdin.readline

def solution(N, board):
    rlen = N
    clen = len(board[0])
    board.append(['_'] * clen)
    head = heart = [0, 0]
    larm = rarm = 0
    min_col, max_col = 1e9, -1e9
    for row in range(rlen):
        for col in range(clen):
            if head == [0, 0] and board[row][col] == '*':
                head = [row, col]
                heart = [head[0] + 1, head[1]]
            if board[row][col] == '*':
                min_col = min(col, min_col)
                max_col = max(col, max_col)
    larm = heart[1] - min_col
    rarm = max_col - heart[1]

    waist = 0
    while board[heart[0] + waist][heart[1]] == '*':
        waist += 1
    waist -= 1

    leg_pos = [heart[0] + waist, heart[1]]
    ll_pos = [leg_pos[0] + 1, leg_pos[1] - 1]
    rr_pos = [leg_pos[0] + 1, leg_pos[1] + 1]
    lleg = rleg = 0
    while board[ll_pos[0] + lleg][ll_pos[1]] == '*' or board[rr_pos[0] + rleg][rr_pos[1]] == '*':
        if board[ll_pos[0] + lleg][ll_pos[1]] == '*':
            lleg += 1
        if board[rr_pos[0] + rleg][rr_pos[1]] == '*':
            rleg += 1

    print(heart[0] + 1, heart[1] + 1)
    print(*[larm, rarm, waist, lleg, rleg], sep = ' ')

N = int(input())
board = [list(input().strip()) for _ in range(N)]
solution(N, board)