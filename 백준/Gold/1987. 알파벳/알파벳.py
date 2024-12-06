drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(R, C, board):

    def dfs(row, col, curr, count):
        nonlocal answer
        answer = max(answer, count)
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if 0 <= nrow < R and 0 <= ncol < C and not cache[ord(board[nrow][ncol]) - 65]:
                cache[ord(board[nrow][ncol]) - 65] = 1
                count += 1
                dfs(nrow, ncol, curr, count)
                count -= 1
                cache[ord(board[nrow][ncol]) - 65] = 0

    cache = [0] * 26
    cache[ord(board[0][0]) - 65] = 1
    answer = 1
    dfs(0, 0, cache, 1)

    return answer

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
print(solution(R, C, board))