import sys
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(m, n, positions):
    field = [[0] * m for _ in range(n)]
    for col, row in positions:
        field[row][col] = 1

    def DFS(r, c):
        field[r][c] = 0
        for d in range(4):
            nx = r + dx[d]
            ny = c + dy[d]
            if (0 <= nx < n) and (0 <= ny < m) and field[nx][ny] == 1:
                DFS(nx, ny)

    answer = 0
    for row in range(n):
        for col in range(m):
            if field[row][col] == 1:
                answer += 1
                DFS(row, col)
    return answer

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    positions = [list(map(int, input().split())) for _ in range(k)]
    print(solution(m, n, positions))
