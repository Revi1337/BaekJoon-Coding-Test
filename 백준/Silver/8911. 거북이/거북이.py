import sys

input = sys.stdin.readline

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(_, dirs):
    for dir in dirs:
        pos = [244, 244]
        positions = [[244, 244]]
        curr_dir = 0
        for d in dir:
            if d == 'L':
                curr_dir = (curr_dir - 1) % 4
            elif d == 'R':
                curr_dir = (curr_dir + 1) % 4
            else:
                if d == 'F':
                    pos[0] += direction[curr_dir][0]
                    pos[1] += direction[curr_dir][1]
                    positions.append([pos[0], pos[1]])
                else:
                    pos[0] += direction[curr_dir][0] * -1
                    pos[1] += direction[curr_dir][1] * -1
                    positions.append([pos[0], pos[1]])

        min_row = min_col = 1e9
        max_row = max_col = -1e9
        for row, col in positions:
            min_row, min_col = min(min_row, row), min(min_col, col)
            max_row, max_col = max(max_row, row), max(max_col, col)

        print(abs(max_row - min_row) * abs(max_col - min_col))


T = int(input())
dirs = [input().strip() for _ in range(T)]
solution(T, dirs)
