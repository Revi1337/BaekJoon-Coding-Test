import sys

input = sys.stdin.readline

def solution(n, m, b, board):
    answer = [float('inf')] * 2
    for height in range(257):
        inven_block = 0
        use_block = 0
        for row in range(n):
            for col in range(m):
                if board[row][col] > height:
                    inven_block += board[row][col] - height
                else:
                    use_block += height - board[row][col]

        if use_block <= b + inven_block:
            require_time = inven_block * 2 + use_block
            if require_time <= answer[0]:
                answer[0] = require_time
                answer[1] = height

    return " ".join(map(str, answer))

n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, b, board))
