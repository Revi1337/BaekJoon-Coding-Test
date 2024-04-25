import sys

input = sys.stdin.readline

def solution(pos):
    board = [[0] * 101 for _ in range(101)]
    for (c1, r1, c2, r2) in pos:
        for row in range(r1, r1 + (r2 - r1)):
            for col in range(c1, c1 + (c2 - c1)):
                board[row][col] = 1

    answer = 0
    for row in range(101):
        for col in range(101):
            if board[row][col]:
                answer += 1

    return answer
pos = [list(map(int, input().split())) for _ in range(4)]
print(solution(pos))

