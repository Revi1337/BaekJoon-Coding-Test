from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(maps):
    row_cnt, col_cnt = len(maps), len(maps[0])
    check = [[[0 for _ in range(2)] for _ in range(col_cnt)] for _ in range(row_cnt)]
    end_row = end_col = -1

    queue = deque()
    for row in range(row_cnt):
        for col in range(col_cnt):
            if maps[row][col] == 'S':
                queue.append((row, col, 0, 0))
                check[row][col][0] = 1
            if maps[row][col] == 'E':
                end_row, end_col = row, col

    while queue:
        row, col, touch, time = queue.popleft()
        if row == end_row and col == end_col and touch == 1:
            return time
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < row_cnt) and (0 <= ncol < col_cnt) and (maps[nrow][ncol] != 'X'):
                if not check[nrow][ncol][touch]:
                    if maps[nrow][ncol] == 'L':
                        check[nrow][ncol][touch] = time + 1
                        queue.append((nrow, ncol, 1, time + 1))
                    else:
                        check[nrow][ncol][touch] = time + 1
                        queue.append((nrow, ncol, touch, time + 1))
    return -1
