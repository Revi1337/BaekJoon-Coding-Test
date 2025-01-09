drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

from collections import deque

def solution(N, board):
    answer, ssize, gage = 0, 2, 2
    sr = sc = None
    for row in range(N):
        for col in range(N):
            if board[row][col] == 9:
                sr, sc = row, col
                board[sr][sc] = 0
                break

    queue = deque()
    while True:
        distance = [[-1] * N for _ in range(N)]
        distance[sr][sc] = 0
        queue.append((sr, sc))

        possible, poss_length = [], 0
        while queue:
            row, col = queue.popleft()
            if (row, col) != (sr, sc) and board[row][col] != 0 and board[row][col] < ssize:
                possible.append((row, col, distance[row][col]))
                poss_length += 1
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if not (0 <= nrow < N and 0 <= ncol < N):
                    continue
                if distance[nrow][ncol] != -1:
                    continue
                if board[nrow][ncol] <= ssize:
                    distance[nrow][ncol] = distance[row][col] + 1
                    queue.append((nrow, ncol))

        if not possible:
            return answer

        possible.sort(key = lambda x: (x[2], x[0], x[1]))
        frow, fcol, dist = possible[0]

        board[frow][fcol] = 0
        sr, sc = frow, fcol
        gage -= 1

        if gage == 0:
            ssize += 1
            gage = ssize

        answer += dist

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))