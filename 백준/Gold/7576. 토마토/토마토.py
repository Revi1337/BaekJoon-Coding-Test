from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(col_cnt, row_cnt, board):
    tomato_pos = []
    counter = 0
    early_return = True
    for row in range(row_cnt):
        for col in range(col_cnt):
            if board[row][col] == 1:
                tomato_pos.append((row, col))
                early_return = early_return and True
            else:
                early_return = early_return and False
            if board[row][col] == 0:
                counter += 1

    if early_return: return 0

    queue = deque()
    check = {*tomato_pos}
    queue.extend(tomato_pos)
    level = 0
    while queue:
        node_cnt = len(queue)
        for _ in range(node_cnt):
            row, col = queue.popleft()
            for d in range(4):
                nrow = row + drow[d]
                ncol = col + dcol[d]
                if (
                        (0 <= nrow < row_cnt)
                            and
                        (0 <= ncol < col_cnt)
                            and
                        (board[nrow][ncol] == 0 and board[nrow][ncol] != -1)
                            and
                        ((nrow, ncol) not in check)
                ):
                    counter -= 1
                    check.add((nrow, ncol))
                    queue.append((nrow, ncol))
        level += 1

        if not counter:
            return 0 if level == 1 else level

    return -1

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, board))
