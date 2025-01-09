drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, likes):
    cost = [0, 1, 10, 100, 1000]
    board = [[0] * N for _ in range(N)]
    table = [[] for _ in range(((N ** 2) + 1))]
    for stu, *prefer in likes:
        table[stu] = {*prefer}

    for stu, *prefer in likes:
        poss = []
        for row in range(N):
            for col in range(N):
                if board[row][col]:
                    continue
                pcnt = ecnt = 0
                for d in range(4):
                    nrow, ncol = row + drow[d], col + dcol[d]
                    if not (0 <= nrow < N and 0 <= ncol < N):
                        continue
                    if board[nrow][ncol] == 0:
                        ecnt += 1
                    elif board[nrow][ncol] in table[stu]:
                        pcnt += 1
                poss.append((row, col, pcnt, ecnt))

        poss.sort(key = lambda x: (-x[2], -x[3], x[0], x[1]))
        row, col, *_ = poss[0]
        board[row][col] = stu

    answer = 0
    for row in range(N):
        for col in range(N):
            pcnt = 0
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if not (0 <= nrow < N and 0 <= ncol < N):
                    continue
                if board[nrow][ncol] in table[board[row][col]]:
                    pcnt += 1
            answer += cost[pcnt]

    return answer

N = int(input())
likes = [list(map(int, input().split())) for _ in range(N ** 2)]
print(solution(N, likes))