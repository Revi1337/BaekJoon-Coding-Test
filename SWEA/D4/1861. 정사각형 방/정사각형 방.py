from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, board):

    def bfs(r, c):
        queue = deque([(r, c, 1)])
        check = [[0] * N for _ in range(N)]
        check[r][c] = 1
        distance = 1

        while queue:
            row, col, dis = queue.popleft()
            distance = max(distance, dis)
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if 0 <= nrow < N and 0 <= ncol < N:
                    if board[nrow][ncol] - board[row][col] == 1 and not check[nrow][ncol]:
                        check[nrow][ncol] = check[row][col] + 1
                        queue.append((nrow, ncol, dis + 1))

        return distance

    collect = []
    for row in range(N):
        for col in range(N):
            collect.append((board[row][col], bfs(row, col)))

    max_answer = max(collect, key=lambda x: x[1])
    answers = []
    for ans in collect:
        if ans[1] == max_answer[1]:
            answers.append(ans)

    answer = min(answers, key=lambda x: x[0])

    return f'{answer[0]} {answer[1]}'

T = int(input())
for index in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{index + 1} {solution(N, board)}')