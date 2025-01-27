sand_ratios = [
    [(-1, 1, 0.01), (1, 1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05)],
    [(-1, -1, 0.01), (-1, 1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (1, -1, 0.1), (1, 1, 0.1), (2, 0, 0.05)],
    [(-1, -1, 0.01), (1, -1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (-1, 1, 0.1), (1, 1, 0.1), (0, 2, 0.05)],
    [(1, -1, 0.01), (1, 1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (-1, -1, 0.1), (-1, 1, 0.1), (-2, 0, 0.05)]
]

drow = [0, 1, 0, -1]
dcol = [-1, 0, 1, 0]

def spread_sand(N, board, row, col, d):
    outside_sand = 0
    total_sand = board[row][col]
    board[row][col] = 0

    for dr, dc, ratio in sand_ratios[d]:
        nr, nc = row + dr, col + dc
        moved_sand = int(total_sand * ratio)
        if 0 <= nr < N and 0 <= nc < N:
            board[nr][nc] += moved_sand
        else:
            outside_sand += moved_sand

    nr, nc = row + drow[d], col + dcol[d]
    remaining_sand = total_sand - sum(int(total_sand * r[2]) for r in sand_ratios[d])
    if 0 <= nr < N and 0 <= nc < N:
        board[nr][nc] += remaining_sand
    else:
        outside_sand += remaining_sand

    return outside_sand

def solution(N, board):
    row = col = N // 2
    d = outside_sand = 0
    step = 1

    while True:
        for _ in range(2):
            for _ in range(step):
                row += drow[d]
                col += dcol[d]
                outside_sand += spread_sand(N, board, row, col, d)
                if row == 0 and col == 0:
                    return outside_sand
            d = (d + 1) % 4
        step += 1

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))