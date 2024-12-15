from itertools import permutations
import copy

# 우, 하, 좌, 상
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

def rotate(board, r, c, s):
    for layer in range(1, s + 1):
        row, col = r - layer, c - layer
        prev = board[row][col]
        for d in range(4):
            while True:
                nrow, ncol = row + drow[d], col + dcol[d]
                if nrow < r - layer or nrow > r + layer or ncol < c - layer or ncol > c + layer:
                    break
                board[nrow][ncol], prev = prev, board[nrow][ncol]
                row, col = nrow, ncol

def get_min_row_sum(board):
    return min(sum(row) for row in board)

def solution(N, M, K, board, rots):
    answer = float('inf')
    for order in permutations(rots):
        n_board = copy.deepcopy(board)
        for r, c, s in order:
            rotate(n_board, r - 1, c - 1, s)
        answer = min(answer, get_min_row_sum(n_board))

    return answer

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rots = [tuple(map(int, input().split())) for _ in range(K)]

print(solution(N, M, K, board, rots))