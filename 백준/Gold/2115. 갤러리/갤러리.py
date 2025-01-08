def solution(M, N, board):
    up, right, down, left = [[[0] * N for _ in range(M)] for _ in range(4)]

    answer = 0
    for row in range(1, M - 1):
        for col in range(1, N - 1):
            if board[row][col] == '.':
                if board[row][col + 1] == '.':
                    if board[row - 1][col] == 'X' and board[row - 1][col + 1] == 'X' and not up[row][col]:
                        up[row][col] = up[row][col + 1] = 1
                        answer += 1
                    if board[row + 1][col] == 'X' and board[row + 1][col + 1] == 'X' and not down[row][col]:
                        down[row][col] = down[row][col + 1] = 1
                        answer += 1
                if board[row + 1][col] == '.':
                    if board[row][col - 1] == 'X' and board[row + 1][col - 1] == 'X' and not left[row][col]:
                        left[row][col] = left[row + 1][col] = 1
                        answer += 1
                    if board[row][col + 1] == 'X' and board[row + 1][col + 1] == 'X' and not right[row][col]:
                        right[row][col] = right[row + 1][col] = 1
                        answer += 1

    return answer

M, N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(M)]
print(solution(M, N, board))
