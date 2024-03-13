import sys

input = sys.stdin.readline

def solution(n, m, board):
    answer = float('inf')
    for row in range(n - 7):
        for col in range(m - 7):
            idx1 = idx2 = 0
            for nrow in range(row, row + 8):
                for ncol in range(col, col + 8):
                    if (nrow + ncol) % 2 == 0:
                        if board[nrow][ncol] != 'W':
                            idx1 += 1
                        if board[nrow][ncol] != 'B':
                            idx2 += 1
                    else:
                        if board[nrow][ncol] != 'B':
                            idx1 += 1
                        if board[nrow][ncol] != 'W':
                            idx2 += 1
            answer = min(answer, min(idx1, idx2))

    return answer


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
print(solution(n, m, board))
