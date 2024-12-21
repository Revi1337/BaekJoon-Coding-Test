from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(board):

    def bfs(row, col):
        vv = [[0] * 5 for _ in range(5)]
        vv[row][col] = 1
        queue = deque([(row, col)])
        cnt = 1
        while queue:
            r, c = queue.popleft()
            for d in range(4):
                nr, nc = r + drow[d], c + dcol[d]
                if 0 <= nr < 5 and 0 <= nc < 5 and not vv[nr][nc] and v[nr][nc]:
                    queue.append((nr, nc))
                    vv[nr][nc] = 1
                    cnt += 1
        return cnt == 7

    def check():
        for row in range(5):
            for col in range(5):
                if v[row][col]:
                    return bfs(row, col)

    def backtracking(n, cnt, scnt):
        if cnt > 7:
            return

        if n == 25:
            if cnt == 7 and scnt >= 4:
                if check():
                    nonlocal answer
                    answer += 1
            return

        v[n // 5][n % 5] = 1
        backtracking(n + 1, cnt + 1, scnt + int(board[n // 5][n % 5] == 'S'))
        v[n // 5][n % 5] = 0
        backtracking(n + 1, cnt, scnt)

    v = [[0] * 5 for _ in range(5)]
    answer = 0
    backtracking(0, 0, 0)

    return answer

board = [list(input().rstrip()) for _ in range(5)]
print(solution(board))