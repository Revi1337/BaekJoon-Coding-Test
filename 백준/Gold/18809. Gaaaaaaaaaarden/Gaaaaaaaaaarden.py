from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, G, R, board):

    def bfs(glst, rlst):
        cnt = 0
        queue = deque()
        check = [[0] * (M + 2) for _ in range(N + 2)]

        for idx in range(R):
            queue.append((rlst[idx][0], rlst[idx][1]))
            check[rlst[idx][0]][rlst[idx][1]] = -1
        for idx in range(G):
            queue.append((glst[idx][0], glst[idx][1]))
            check[glst[idx][0]][glst[idx][1]] = 1

        while queue:
            row, col = queue.popleft()
            if check[row][col] == 25000:
                continue
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if board[nrow][ncol] == 0 or check[nrow][ncol] == 25000:
                    continue

                if check[nrow][ncol] == 0:
                    if check[row][col] < 0:
                        check[nrow][ncol] = check[row][col] - 1
                        queue.append((nrow, ncol))
                    else:
                        check[nrow][ncol] = check[row][col] + 1
                        queue.append((nrow, ncol))
                else:
                    if check[row][col] < 0:
                        if check[nrow][ncol] + check[row][col] - 1 == 0:
                            cnt += 1
                            check[nrow][ncol] = 25000
                    else:
                        if check[nrow][ncol] + check[row][col] + 1 == 0:
                            cnt += 1
                            check[nrow][ncol] = 25000

        return cnt

    def backtracking(n, gcnt, rcnt, glst, rlst):
        if n == poss_length:
            if gcnt == G and rcnt == R:
                nonlocal answer
                answer = max(answer, bfs(glst, rlst))
            return

        if colors[0]:
            colors[0] -= 1
            backtracking(n + 1, gcnt + 1, rcnt, glst + [poss[n]], rlst)
            colors[0] += 1
        if colors[1]:
            colors[1] -= 1
            backtracking(n + 1, gcnt, rcnt + 1, glst, rlst + [poss[n]])
            colors[1] += 1
        backtracking(n + 1, gcnt, rcnt, glst, rlst)

    poss = []
    for row in range(1, N + 1):
        for col in range(1, M + 1):
            if board[row][col] == 2:
                poss.append((row, col))

    colors = [G, R]
    poss_length = len(poss)

    answer = 0
    backtracking(0, 0, 0, [], [])

    return answer

N, M, G, R = map(int, input().split())
board = [[0] * (M + 2)] + [[0] + list(map(int, input().split()))+[0] for _ in range(N)] + [[0] * (M + 2)]
print(solution(N, M, G, R, board))
