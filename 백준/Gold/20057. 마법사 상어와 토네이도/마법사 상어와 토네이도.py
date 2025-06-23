drow = [0, 1, 0, -1]
dcol = [-1, 0, 1, 0]
rates = [
    [(-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (1, 1, 0.01), (1, 0, 0.07), (1, -1, 0.1), (0, -2, 0.05), (-2, 0, 0.02), (2, 0, 0.02)],
    [(-1, -1, 0.01), (-1, 1, 0.01), (0, 1, 0.07), (0, 2, 0.02), (1, 1, 0.1), (2, 0, 0.05), (1, -1, 0.1), (0, -1, 0.07), (0, -2, 0.02)],
    [(-1, -1, 0.01), (-2, 0, 0.02), (-1, 0, 0.07), (-1, 1, 0.1), (0, 2, 0.05), (1, 1, 0.1), (1, 0, 0.07), (2, 0, 0.02), (1, -1, 0.01)],
    [(-1, -1, 0.1), (-2, 0, 0.05), (-1, 1, 0.1), (0, 1, 0.07), (0, 2, 0.02), (1, 1, 0.01), (1, -1, 0.01), (0, -1, 0.07), (0, -2, 0.02)]
]

def solution(N, board):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    def spread(srow, scol, d):
        out = 0
        curr = board[srow][scol]

        for dr, dc, ratio in rates[d]:
            nrow, ncol = srow + dr, scol + dc
            mv = int(curr * ratio)
            if inside(nrow, ncol):
                board[nrow][ncol] += mv
            else:
                out += mv

        nrow, ncol = srow + drow[d], scol + dcol[d]
        remain = curr - sum(int(curr * r[2]) for r in rates[d])
        if inside(nrow, ncol):
            board[nrow][ncol] += remain
        else:
            out += remain

        return out

    srow, scol = N // 2, N // 2
    answer, dir, step = 0, 0, 1

    while True:
        for _ in range(2):
            for _ in range(step):
                nrow, ncol = srow + drow[dir], scol + dcol[dir]
                answer += spread(nrow, ncol, dir)
                srow, scol = nrow, ncol
                if (srow, scol) == (0, 0):
                    return answer
            dir = (dir + 1) % 4
        step += 1

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))
