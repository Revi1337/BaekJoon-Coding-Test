import sys

sys.setrecursionlimit(10 ** 5)

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def dfs(row, col):
    check[row][col] = 1
    for d in range(4):
        nrow = row + drow[d]
        ncol = col + dcol[d]
        if (0 <= nrow < n) and (0 <= ncol < n) and (blocks[nrow][ncol] > height) and (check[nrow][ncol] == 0):
            dfs(nrow, ncol)

minN = 100_000_000
maxN = -100_000_000
n = int(input())
blocks = []
for _ in range(n):
    integers = list(map(int, input().split()))
    for integer in integers:
        if integer < minN:
            minN = integer
        if integer > maxN:
            maxN = integer
    blocks.append(integers)

res = -100_000_000
for height in range(0, maxN + 1):
    check = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and blocks[i][j] > height:
                dfs(i, j)
                cnt += 1
    res = max(res, cnt)

print(res)