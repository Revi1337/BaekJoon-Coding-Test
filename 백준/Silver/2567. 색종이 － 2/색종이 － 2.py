drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, pos):
    paper = [[0] * 102 for _ in range(102)]
    for x, y in pos:
        for row in range(y + 1, y + 11):
            for col in range(x + 1, x + 11):
                paper[row][col] = 1

    answer = 0
    for row in range(102):
        for col in range(102):
            if paper[row][col]:
                for d in range(4):
                    nrow, ncol = row + drow[d], col + dcol[d]
                    if paper[nrow][ncol] == 0:
                        answer += 1

    return answer

N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, pos))

