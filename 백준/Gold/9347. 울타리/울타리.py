from collections import deque

INF = 1e9
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(R, C, board):
    queue = deque()
    check = [[INF] * C for _ in range(R)]

    for row in range(R):
        for col in range(C):
            if row in [0, R - 1] or col in [0, C - 1]:
                if board[row][col]:
                    queue.append((board[row][col], row, col))
                else:
                    queue.appendleft((board[row][col], row, col))

    while queue:
        cost, row, col = queue.popleft()
        if cost > check[row][col]:
            continue

        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if 0 <= nrow < R and 0 <= ncol < C:
                if board[nrow][ncol] == 0 and cost < check[nrow][ncol]:
                    check[nrow][ncol] = cost
                    queue.appendleft((cost, nrow, ncol))
                elif board[nrow][ncol] == 1 and cost + 1 < check[nrow][ncol]:
                    check[nrow][ncol] = cost + 1
                    queue.append((cost + 1, nrow, ncol))

    mcnt = [0] * (R * C + 1)
    mcost = 0

    for row in range(R):
        for col in range(C):
            if board[row][col] == 0:
                mcnt[check[row][col]] += 1
                mcost = max(mcost, check[row][col])

    return f'{mcost} {mcnt[mcost]}'


T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    print(solution(R, C, board))