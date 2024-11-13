from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

"""
bfs
"""
def solution(board):

    queue = deque()

    st = []
    end = []
    check = [[0] * 16 for _ in range(16)]

    for row in range(16):
        for col in range(16):
            if board[row][col] == 2:
                st = [row, col]
            if board[row][col] == 3:
                end = [row, col]

    queue.append((st[0], st[1]))
    check[st[0]][st[1]] = 1

    while queue:
        row, col = queue.popleft()
        if (row, col) == (end[0], end[1]):
            return 1
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if (0 <= nrow < 16) and (0 <= ncol < 16):
                if (board[nrow][ncol] != 1) and not check[nrow][ncol]:
                    queue.append((nrow, ncol))
                    check[nrow][ncol] = 1

    return 0

T = 10
for _ in range(T):
    index = int(input())
    board = [list(map(int, list(input().rstrip()))) for _ in range(16)]
    print(f'#{index} {solution(board)}')