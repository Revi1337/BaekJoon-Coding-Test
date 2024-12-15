from itertools import permutations

# 우, 하, 좌, 상
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

def rotate(n_board, rr, rc, t):
    to, fro = [rr - t - 1, rc - t - 1], [rr + t - 1, rc + t - 1]
    offset = 0
    while offset < t:
        row, col, d = to[0], to[1] + 1, 0
        prev = n_board[to[0]][to[1]]
        while [row, col] != to:
            nrow, ncol = row + drow[d], col + dcol[d]
            if not (to[0] <= nrow <= fro[0] and to[1] <= ncol <= fro[1]):
                d = (d + 1) % 4
                continue
            n_board[row][col], prev = prev, n_board[row][col]
            row, col = nrow, ncol
        n_board[row][col] = prev
        offset += 1
        to = [to[0] + 1, to[1] + 1]
        fro = [fro[0] - 1, fro[1] - 1]

def solution(N, M, K, board, rots):
    answer = float('inf')
    for rotators in permutations(rots, K):
        n_board = [[*line] for line in board]
        for rr, rc, t in rotators:
            rotate(n_board, rr, rc, t)
        minN = min([sum(line) for line in n_board])
        answer = min(answer, minN)

    return answer

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rots = [list(map(int, input().split())) for _ in range(K)]
print(solution(N, M, K, board, rots))