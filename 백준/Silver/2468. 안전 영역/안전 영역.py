from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def valid_direction():
    return (0 <= nrow < n) and (0 <= ncol < n) and (blocks[nrow][ncol] > height) and (check[nrow][ncol] == 0)

n = int(input())
minN = 100_000_000
maxN = -100_000_000
blocks = []
for _ in range(n):
    integers = list(map(int, input().split()))
    minN = min(minN, min(integers))
    maxN = max(maxN, max(integers))
    blocks.append(integers)

answer = -100_000_000
for height in range(0, maxN + 1):
    check = [[0] * n for _ in range(n)]
    queue = deque()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and blocks[i][j] > height:
                queue.append([i, j])
                check[i][j] = 0
                cnt += 1
                while queue:
                    row, col = queue.popleft()
                    for d in range(4):
                        nrow = row + drow[d]
                        ncol = col + dcol[d]
                        if valid_direction():
                            check[nrow][ncol] = 1
                            queue.append([nrow, ncol])
                answer = max(answer, cnt)

print(answer)
