import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(n, rooms):
    rooms[0][0] = -1
    queue = deque([(0, 0, 0)])
    while queue:
        row, col, cnt = queue.popleft()
        if (row, col) == (n - 1, n - 1):
            return cnt
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < n) and (0 <= ncol < n) and (rooms[nrow][ncol] != -1):
                if rooms[nrow][ncol] == 1:
                    queue.appendleft((nrow, ncol, cnt))
                elif not rooms[nrow][ncol]:
                    queue.append((nrow, ncol, cnt + 1))
                rooms[nrow][ncol] = -1

n = int(input())
rooms = [list(map(int, input().rstrip())) for _ in range(n)]
print(solution(n, rooms))

