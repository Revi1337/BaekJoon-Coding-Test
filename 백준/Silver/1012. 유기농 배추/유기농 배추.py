from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solution(m, n, positions):
    field = [[0] * m for _ in range(n)]
    for col, row in positions:
        field[row][col] = 1

    queue = deque()
    answer = 0
    for row in range(n):
        for col in range(m):
            if field[row][col] == 1:
                answer += 1
                queue.append([row, col])
                while queue:
                    node_cnt = len(queue)
                    for _ in range(node_cnt):
                        r, c = queue.popleft()
                        for d in range(4):
                            nr = r + dr[d]
                            nc = c + dc[d]
                            if (0 <= nr < n) and (0 <= nc < m) and field[nr][nc] == 1:
                                queue.append([nr, nc])
                                field[nr][nc] = 0
    return answer

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    positions = [list(map(int, input().split())) for _ in range(k)]
    print(solution(m, n, positions))
