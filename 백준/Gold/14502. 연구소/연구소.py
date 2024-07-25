import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, board):
    virus = []
    answer = -1e9
    for row in range(N):
        for col in range(M):
            if board[row][col] == 2:
                virus.append((row, col))

    def dfs(count):
        if count == 3:
            bfs()
            return
        for row in range(N):
            for col in range(M):
                if board[row][col] == 0:
                    board[row][col] = 1
                    dfs(count + 1)
                    board[row][col] = 0

    def bfs():
        queue = deque(virus)
        check = [[0] * M for _ in range(N)]
        for row in range(N):
            for col in range(M):
                check[row][col] = board[row][col]

        while queue:
            row, col = queue.popleft()
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if (0 <= nrow < N) and (0 <= ncol < M) and (not check[nrow][ncol]):
                    check[nrow][ncol] = 2
                    queue.append((nrow, ncol))

        ans = 0
        for row in range(N):
            for col in range(M):
                if check[row][col] == 0:
                    ans += 1
        nonlocal answer
        answer = max(answer, ans)

    dfs(0)

    return answer

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
