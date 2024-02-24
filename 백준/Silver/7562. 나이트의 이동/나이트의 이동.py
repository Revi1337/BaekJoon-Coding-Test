from collections import deque

drow = [-2, -2, -1, 1, 2, 2, 1, -1]
dcol = [-1, 1, 2, 2, 1, -1, -2, -2]

def solution(board_length, curr_pos, target_pos):
    board = [[0] * board_length for _ in range(board_length)]

    start_row, start_col = curr_pos
    end_row, end_col = target_pos

    queue = deque([(start_row, start_col)])
    board[start_row][start_col] = 1
    level = 0
    while queue:
        node_cnt = len(queue)
        for _ in range(node_cnt):
            row, col = queue.popleft()
            if (row == end_row) and (col == end_col):
                return level
            for d in range(8):
                nrow = row + drow[d]
                ncol = col + dcol[d]
                if (
                        (0 <= nrow < board_length)
                            and
                        (0 <= ncol < board_length)
                            and
                        (not board[nrow][ncol])
                ):
                    board[nrow][ncol] = 1
                    queue.append((nrow, ncol))
        level += 1

    return level

loop = int(input())
for _ in range(loop):
    board_length = int(input())
    curr_pos = list(map(int, input().split()))
    target_pos = list(map(int, input().split()))
    print(solution(board_length, curr_pos, target_pos))
