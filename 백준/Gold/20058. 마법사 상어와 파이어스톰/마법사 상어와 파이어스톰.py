from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, Q, ices, opers):
    N = 2 ** N

    def bfs(srow, scol):
        queue = deque([(srow, scol)])
        check[srow][scol] = 1
        cnt = 1

        while queue:
            row, col = queue.popleft()
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if 0 <= nrow < N and 0 <= ncol < N and not check[nrow][ncol] and ices[nrow][ncol] > 0:
                    queue.append((nrow, ncol))
                    check[nrow][ncol] = 1
                    cnt += 1
        return cnt

    def decrease_ice():
        to_decrease = []
        for row in range(N):
            for col in range(N):
                if ices[row][col] == 0:
                    continue
                count = 0
                for d in range(4):
                    nr, nc = row + drow[d], col + dcol[d]
                    if 0 <= nr < N and 0 <= nc < N and ices[nr][nc] > 0:
                        count += 1
                if count < 3:
                    to_decrease.append((row, col))
        for row, col in to_decrease:
            ices[row][col] -= 1

    def rotate(futures, s):
        rotated = [[0] * s for _ in range(s)]
        for row in range(s):
            for col in range(s):
                rotated[col][s - 1 - row] = futures[row][col]
        return rotated

    def modify(r, s):
        if r >= N:
            return

        for offset in range(N // s):
            future = []
            for row in ices[r : r + s]:
                future.append(row[offset * s : (offset + 1) * s])

            rotated = rotate(future, s)
            for i in range(s):
                for j in range(s):
                    ices[r + i][offset * s + j] = rotated[i][j]
        modify(r + s, s)

    for oper in opers:
        size = 2 ** oper
        modify(0, size)
        decrease_ice()

    total = sum(sum(row) for row in ices)
    check = [[0] * N for _ in range(N)]
    mx_cnt = 0
    for r in range(N):
        for c in range(N):
            if not check[r][c] and ices[r][c] > 0:
                mx_cnt = max(mx_cnt, bfs(r, c))

    print(total)
    print(mx_cnt)

N, Q = map(int, input().split())
ices = [list(map(int, input().split())) for _ in range(2 ** N)]
opers = list(map(int, input().split()))
solution(N, Q, ices, opers)