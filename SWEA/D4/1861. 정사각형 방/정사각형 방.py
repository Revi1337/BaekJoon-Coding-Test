from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, board):
    possible = []

    for row in range(N):
        for col in range(N):
            queue = deque([(row, col, 1)])
            check = [[0] * N for _ in range(N)]
            check[row][col] = 1
            distance = 1

            while queue:
                r, c, dis = queue.popleft()
                distance = max(distance, dis)
                for d in range(4):
                    nrow, ncol = r + drow[d], c + dcol[d]
                    if 0 <= nrow < N and 0 <= ncol < N:
                        if board[nrow][ncol] - board[r][c] == 1 and not check[nrow][ncol]:
                            check[nrow][ncol] = check[r][c] + 1
                            queue.append((nrow, ncol, dis + 1))

            possible.append((board[row][col], distance))

    max_answer = max(possible, key=lambda x: x[1])
    answers = []
    for ans in possible:
        if ans[1] == max_answer[1]:
            answers.append(ans)

    answer = min(answers, key=lambda x: x[0])

    return f'{answer[0]} {answer[1]}'

T = int(input())
for index in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{index + 1} {solution(N, board)}')
