import sys

input = sys.stdin.readline

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(R, C, maps):
    future_change = []
    for row in range(R):
        for col in range(C):
            if maps[row][col] == 'X':
                counter = 0
                for r, c in (-1, 0), (0, 1), (1, 0), (0, -1):
                    nrow, ncol = row + r, col + c
                    if (0 <= nrow < R) and (0 <= ncol < C):
                        if maps[nrow][ncol] == '.':
                            counter += 1
                    else:
                        counter += 1
                if counter >= 3:
                    future_change.append((row, col))

    for row, col in future_change:
        maps[row][col] = '.'

    min_row = min_col = 1e9
    max_row = max_col = -1e9
    for row in range(R):
        for col in range(C):
            if maps[row][col] == 'X':
                min_row, min_col = min(min_row, row), min(min_col, col)
                max_row, max_col = max(max_row, row), max(max_col, col)

    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            print(maps[row][col], end = '')
        print()


R, C = map(int, input().split())
maps = [list(input().strip()) for _ in range(R)]
solution(R, C, maps)