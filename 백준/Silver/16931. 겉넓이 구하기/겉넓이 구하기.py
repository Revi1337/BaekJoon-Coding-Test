import sys

input = sys.stdin.readline

def solution(N, M, paper):
    answer = N * M
    for col in range(M):
        for row in range(N):
            if row == 0:
                answer += paper[row][col]
            else:
                if paper[row][col] > paper[row - 1][col]:
                    answer += paper[row][col] - paper[row - 1][col]

    for row in range(N):
        for col in range(M):
            if col == 0:
                answer += paper[row][col]
            else:
                if paper[row][col] > paper[row][col - 1]:
                    answer += paper[row][col] - paper[row][col - 1]

    return answer * 2


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, paper))
