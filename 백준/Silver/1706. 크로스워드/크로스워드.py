import sys

input = sys.stdin.readline

def solution(R, C, board):
    answer = []
    for row in range(R):
        line = board[row]
        words = line.split('#')
        for word in words:
            if len(word) >= 2:
                answer.append(word)

    for col in range(C):
        line = "".join([row[col] for row in board])
        words = line.split('#')
        for word in words:
            if len(word) >= 2:
                answer.append(word)

    answer.sort()
    return answer[0]

R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]
print(solution(R, C, board))