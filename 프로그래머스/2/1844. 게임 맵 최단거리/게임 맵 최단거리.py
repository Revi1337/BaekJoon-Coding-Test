from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(maps):
    row_cnt = len(maps)
    col_cnt = len(maps[0])
    queue = deque()
    check = set()
    distance = [[0] * col_cnt for _ in range(row_cnt)]

    queue.append((0, 0))
    check.add((0, 0))
    distance[0][0] = 1

    while queue:
        row, col = queue.popleft()
        if distance[row_cnt - 1][col_cnt - 1] != 0:
            return distance[row_cnt - 1][col_cnt - 1]
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < row_cnt) and (0 <= ncol < col_cnt) and (maps[nrow][ncol]) and ((nrow, ncol) not in check):
                distance[nrow][ncol] = distance[row][col] + 1
                check.add((nrow, ncol))
                queue.append((nrow, ncol))

    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))