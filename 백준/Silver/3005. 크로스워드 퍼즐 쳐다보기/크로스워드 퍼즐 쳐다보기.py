import sys

input = sys.stdin.readline

def solution(R, C, board):
    words = []
    for row in range(R):
        line = "".join(board[row])
        data = line.split('#')
        for d in data:
            if len(d) > 1:
                words.append(d)

    for col in range(C):
        line = "".join([row[col] for row in board])
        data = line.split('#')
        for d in data:
            if len(d) > 1:
                words.append(d)

    words.sort()
    return words[0]


R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
print(solution(R, C, board))