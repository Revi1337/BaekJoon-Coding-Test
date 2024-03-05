import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(m, n, miro):
    miro[0][0] = -1
    queue = deque([(0, 0, 0)])
    while queue:
        row, col, cnt = queue.popleft()
        if (row, col) == (n - 1, m - 1):
            return cnt
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < n) and (0 <= ncol < m) and (miro[nrow][ncol] != -1):
                if miro[nrow][ncol] == 0:
                    queue.appendleft((nrow, ncol, cnt))
                elif miro[nrow][ncol] == 1:
                    queue.append((nrow, ncol, cnt + 1))
                miro[nrow][ncol] = -1


m, n = map(int, input().split())
miro = [list(map(int, input().rstrip())) for _ in range(n)]
print(solution(m, n, miro))
