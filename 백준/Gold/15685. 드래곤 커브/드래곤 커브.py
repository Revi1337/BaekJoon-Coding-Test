# 우, 상, 좌, 하
drow = [0, -1, 0, 1]
dcol = [1, 0, -1, 0]

def solution(N, opers):
    board = [[0] * 101 for _ in range(101)]

    for x, y, d, g in opers:
        stack = [[y, x]]
        lrow, lcol = y + drow[d], x + dcol[d]
        stack.append([lrow, lcol])

        for _ in range(g):
            erow, ecol = stack[-1]
            for idx in range(len(stack) - 2, -1, -1):
                crow, ccol = stack[idx]
                stack.append([erow - (ecol - ccol), ecol + (erow - crow)])

        for row, col in stack:
            board[row][col] = 1

    cnt = 0
    for row in range(100):
        for col in range(100):
            if board[row][col] and board[row + 1][col] and board[row][col + 1] and board[row + 1][col + 1]:
                cnt += 1
    return cnt

N = int(input())
opers = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, opers))