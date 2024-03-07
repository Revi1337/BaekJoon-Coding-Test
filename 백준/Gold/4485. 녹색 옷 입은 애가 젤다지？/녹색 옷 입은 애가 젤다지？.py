import sys
import heapq

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(idx, n, field):
    check = [[0] * n for _ in range(n)]
    check[0][0] = 1
    queue = []
    heapq.heappush(queue, (field[0][0], 0, 0))
    while queue:
        cost, row, col = heapq.heappop(queue)
        if (row, col) == (n - 1, n - 1):
            return f'Problem {idx}: {cost}'
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < n) and (0 <= ncol < n) and (not check[nrow][ncol]):
                check[nrow][ncol] = 1
                heapq.heappush(queue, (cost + field[nrow][ncol], nrow, ncol))

idx = 1
while True:
    n = int(input())
    if n == 0:
        break
    field = [list(map(int, input().split())) for _ in range(n)]
    print(solution(idx, n, field))
    idx += 1


