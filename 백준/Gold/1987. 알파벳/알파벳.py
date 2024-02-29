drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(r, c, board):
    answer = 0
    duplicate = [0] * 26

    def dfs(row, col, counter):
        nonlocal answer
        answer = max(answer, counter)
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < r) and (0 <= ncol < c):
                if not duplicate[ord(board[nrow][ncol]) % 26]:
                    duplicate[ord(board[nrow][ncol]) % 26] = 1
                    dfs(nrow, ncol, counter + 1)
                    duplicate[ord(board[nrow][ncol]) % 26] = 0

    duplicate[ord(board[0][0]) % 26] = 1
    dfs(0, 0, 1)
    duplicate[ord(board[0][0]) % 26] = 0

    return answer

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
print(solution(r, c, board))