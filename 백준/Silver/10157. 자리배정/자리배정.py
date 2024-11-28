drow = [-1, 0 ,1, 0]
dcol = [0, 1, 0, -1]

def solution(C, R, K):
    board = [[0] * R for _ in range(C)]

    d = init = 1
    board[0][0] = init
    init += 1
    curr = [0, 0]

    while init <= R * C:
        nrow, ncol = curr[0] + drow[d], curr[1] + dcol[d]
        if not (0 <= nrow < C and 0 <= ncol < R) or board[nrow][ncol]:
            d = (d + 1) % 4
        else:
            board[nrow][ncol] = init
            curr = [nrow, ncol]
            init += 1

    for row in range(C):
        for col in range(R):
            if board[row][col] == K:
                print(row + 1, col + 1, sep = ' ')
                return

    print(0)

C, R = map(int, input().split())
K = int(input())
solution(C, R, K)
