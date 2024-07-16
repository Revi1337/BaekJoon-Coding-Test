import sys

input = sys.stdin.readline

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(C, R, K):
    d = 0
    board = [[0] * C for _ in range(R)]
    pos = [R - 1, 0]
    start = 1
    board[pos[0]][pos[1]] = start
    start += 1
    while start <= C * R:
        nrow, ncol = pos[0] + direction[d][0], pos[1] + direction[d][1]
        if (not ((0 <= nrow < R) and (0 <= ncol < C))) or board[nrow][ncol]:
            d = (d + 1) % 4
        else:
            pos[0], pos[1] = nrow, ncol
            board[pos[0]][pos[1]] = start
            start += 1

    if K > C * R:
        print(0)
    else:
        for row in range(R):
            for col in range(C):
                if board[row][col] == K:
                    print(f'{col + 1} {R - row} ')

C, R = map(int, input().split())
K = int(input())
solution(C, R, K)