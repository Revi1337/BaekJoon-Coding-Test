import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(n, dangers, m, deaths):
    DEATH = 2
    DANGER = 1
    field = [[0 for _ in range(501)] for _ in range(501)]
    for x1, y1, x2, y2 in dangers:
        for row in range(min([x1, x2]), max(x1, x2) + 1):
            for col in range(min([y1, y2]), max(y1, y2) + 1):
                field[row][col] = DANGER

    for x1, y1, x2, y2 in deaths:
        for row in range(min([x1, x2]), max([x1, x2]) + 1):
            for col in range(min([y1, y2]), max([y1, y2]) + 1):
                field[row][col] = DEATH

    queue = deque([(0, 0, 0)])
    while queue:
        row, col, time = queue.popleft()
        if row == 500 and col == 500:
            print(time)
            break
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < 501) and (0 <= ncol < 501):
                if field[nrow][ncol] == 0:
                    field[nrow][ncol] = 2
                    queue.appendleft((nrow, ncol, time))
                elif field[nrow][ncol] == 1:
                    field[nrow][ncol] = 2
                    queue.append((nrow, ncol, time + 1))
    else:
        print(-1)

n = int(input())
dangers = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
deaths = [list(map(int, input().split())) for _ in range(m)]
solution(n, dangers, m, deaths)