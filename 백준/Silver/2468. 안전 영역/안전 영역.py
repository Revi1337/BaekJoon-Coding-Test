from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, board):
    max_height = max([max(heights) for heights in board])

    def bfs(row, col):
        new_board[row][col] = 0
        queue = deque([(row, col)])
        while queue:
            r, c = queue.popleft()
            for d in range(4):
                nr, nc = r + drow[d], c + dcol[d]
                if 0 <= nr < N and 0 <= nc < N and new_board[nr][nc] == 1:
                    new_board[nr][nc] = 0
                    queue.append((nr, nc))

    answer = 0
    for height in range(max_height + 1):
        new_board = [[1] * N for _ in range(N)]
        for row in range(N):
            for col in range(N):
                if board[row][col] <= height:
                    new_board[row][col] = 0

        counter = 0
        for row in range(N):
            for col in range(N):
                if new_board[row][col]:
                    counter += 1
                    bfs(row, col)
        answer = max(answer, counter)

    return answer


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))