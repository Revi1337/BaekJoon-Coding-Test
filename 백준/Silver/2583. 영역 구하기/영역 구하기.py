###### DFS 방법 1 ###### (cnt 를 dfs 의 매개변수에서 활용)
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





###### DFS 방법 2 ###### (cnt 를 별도의 변수로 뺴고 nonlocal 로 접근)
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

    def dfs(row, col):
        nonlocal cnt
        cnt += 1
        paper[row][col] = 1
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < m) and (0 <= ncol < n) and (not paper[nrow][ncol]):
                dfs(nrow, ncol)

    answer = 0
    counter = []
    for row in range(m):
        cnt = 0
        for col in range(n):
            if not paper[row][col]:
                answer += 1
                dfs(row, col)
                counter.append(cnt)
                cnt = 0

    print(answer)
    print(*sorted(counter))

m, n, k = map(int, input().split())
squares = [list(map(int, input().split())) for _ in range(k)]
solution(m, n, k, squares)
