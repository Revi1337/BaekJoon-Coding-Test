from collections import deque
import sys

input = sys.stdin.readline

drow = [-2, -2, 0, 0, 2, 2]
dcol = [-1, 1, -2, 2, -1, 1]

def solution(n, r1, c1, r2, c2):
    check = [[-1 for _ in range(n)] for _ in range(n)]
    check[r1][c1] = 0
    queue = deque([(r1, c1)])
    while queue:
        row, col = queue.popleft()
        if (row, col) == (r2, c2):
            return check[r2][c2]
        for d in range(6):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < n) and (0 <= ncol < n) and (check[nrow][ncol] == -1):
                check[nrow][ncol] = check[row][col] + 1
                queue.append((nrow, ncol))
    return -1

n = int(input().rstrip())
r1, c1, r2, c2 = map(int, input().split())
print(solution(n, r1, c1, r2, c2))