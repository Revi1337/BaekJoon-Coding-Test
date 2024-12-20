from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(R, C, board):
    check = [[set() for _ in range(C)] for _ in range(R)]
    check[0][0].add(board[0][0])
    queue = deque([(0, 0, board[0][0])])

    ans = 1
    while queue:
        row, col, alpha = queue.popleft()
        ans = max(ans, len(alpha))
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if 0 <= nrow < R and 0 <= ncol < C:
                if board[nrow][ncol] not in alpha and alpha + board[nrow][ncol] not in check[nrow][ncol]:
                    check[nrow][ncol].add(alpha + board[nrow][ncol])
                    queue.append((nrow, ncol, alpha + board[nrow][ncol]))

    return ans

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
print(solution(R, C, board))
