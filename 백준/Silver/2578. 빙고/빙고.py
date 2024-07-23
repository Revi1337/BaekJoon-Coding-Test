import sys

input = sys.stdin.readline

def solution(board, questions):
    counter = 0
    for question in questions:
        for q in question:
            for row in range(5):
                for col in range(5):
                    if board[row][col] == q:
                        counter += 1
                        board[row][col] = 0

            answer = 0
            for line in board:
                if sum(line) == 0:
                    answer += 1
                    if answer == 3:
                        return counter

            for col in range(5):
                if sum([line[col] for line in board]) == 0:
                    answer += 1
                    if answer == 3:
                        return counter

            if sum([board[row][5 - row - 1] for row in range(5)]) == 0:
                answer += 1
                if answer == 3:
                    return counter

            if sum([board[row][row] for row in range(5)]) == 0:
                answer += 1
                if answer == 3:
                    return counter

board = [list(map(int, input().split())) for _ in range(5)]
questions = [list(map(int, input().split())) for _ in range(5)]
print(solution(board, questions))


