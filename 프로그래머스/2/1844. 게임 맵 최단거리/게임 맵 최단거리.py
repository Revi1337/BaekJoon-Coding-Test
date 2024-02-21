from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(maps):
    row_cnt = len(maps)
    col_cnt = len(maps[0])
    queue = deque()
    distance = [[0] * col_cnt for _ in range(row_cnt)]

    queue.append((0, 0))
    distance[0][0] = 1
    maps[0][0] = 0

    while queue:
        row, col = queue.popleft()
        if distance[row_cnt - 1][col_cnt - 1] != 0:
            return distance[row_cnt - 1][col_cnt - 1]
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < row_cnt) and (0 <= ncol < col_cnt) and (maps[nrow][ncol]):
                distance[nrow][ncol] = distance[row][col] + 1
                queue.append((nrow, ncol))
                maps[nrow][ncol] = 0

    return -1