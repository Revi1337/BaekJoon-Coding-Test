import sys

input = sys.stdin.readline

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(directions):
    board = [[0] * 100 for _ in range(100)]
    pos = [49, 49]
    board[pos[0]][pos[1]] = '.'
    d = 2
    for dir in directions:
        if dir == 'R':
            d = (d + 1) % 4
        elif dir == 'L':
            d = (d - 1) % 4
        elif dir == 'F':
            pos[0] += direction[d][0]
            pos[1] += direction[d][1]
            board[pos[0]][pos[1]] = '.'

    max_row = max_col = -1e9
    min_row = min_col = 1e9
    for row in range(100):
        for col in range(100):
            if board[row][col] == '.':
                max_row, max_col = max(max_row, row), max(max_col, col)
                min_row, min_col = min(min_row, row), min(min_col, col)

    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if board[row][col] == '.':
                print(board[row][col], end = '')
            else:
                print('#', end = '')
        print()

_ = int(input())
directions = input().strip()
solution(directions)