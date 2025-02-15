from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, board):

    inside = lambda row, col : 0 <= row < N and 0 <= col < M

    def get_trace(srow, scol):
        check[srow][scol] = 1
        queue.append((srow, scol))
        trace = []

        while queue:
            row, col = queue.popleft()
            trace.append((row, col))
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if inside(nrow, ncol) and board[nrow][ncol] == 'L' and not check[nrow][ncol]:
                    check[nrow][ncol] = 1
                    queue.append((nrow, ncol))

        return trace

    def find_max_distance(srow, scol):
        mx = 0
        check = [[0] * M for _ in range(N)]
        check[srow][scol] = 1
        queue.append((srow, scol, 0))

        while queue:
            row, col, distance = queue.popleft()
            mx = max(mx, distance)
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if inside(nrow, ncol) and board[nrow][ncol] == 'L' and not check[nrow][ncol]:
                    check[nrow][ncol] = 1
                    queue.append((nrow, ncol, distance + 1))

        return mx

    queue = deque()
    check = [[0] * M for _ in range(N)]
    availabe = []
    for row in range(N):
        for col in range(M):
            if board[row][col] == 'L' and not check[row][col]:
                availabe.append([*get_trace(row, col)])

    answer = 0
    for trace in availabe:
        for row, col in trace:
            answer = max(answer, find_max_distance(row, col))

    return answer


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
print(solution(N, M, board))