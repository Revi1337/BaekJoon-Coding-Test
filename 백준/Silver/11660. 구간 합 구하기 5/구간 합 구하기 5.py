import sys

input = sys.stdin.readline

def solution(n, board, require):
    prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            prefix_sum[row][col] = \
            prefix_sum[row - 1][col] + prefix_sum[row][col - 1] - prefix_sum[row - 1][col - 1] + board[row - 1][col - 1]

    for i, j, x, y in require:
        print(prefix_sum[x][y] - prefix_sum[i - 1][y] - prefix_sum[x][j - 1] + prefix_sum[i - 1][j - 1])

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
require = [list(map(int, input().split())) for _ in range(m)]
solution(n, board, require)

