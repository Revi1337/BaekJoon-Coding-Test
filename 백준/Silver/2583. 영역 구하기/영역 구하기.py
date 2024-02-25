import sys

sys.setrecursionlimit(10 ** 5)

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(m, n, k, squares):
    paper = [[0] * n for _ in range(m)]
    for start_col, start_row, end_col, end_row in squares:
        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                paper[row][col] = 1

    def dfs(row, col, cnt):
        paper[row][col] = 1
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < m) and (0 <= ncol < n) and (not paper[nrow][ncol]):
                cnt = dfs(nrow, ncol, cnt + 1)
        return cnt

    answer = 0
    counter = []
    for row in range(m):
        for col in range(n):
            if not paper[row][col]:
                answer += 1
                cnt = dfs(row, col, 1)
                counter.append(cnt)

    print(answer)
    print(*sorted(counter))

m, n, k = map(int, input().split())
squares = [list(map(int, input().split())) for _ in range(k)]
solution(m, n, k, squares)