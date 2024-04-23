import sys

input = sys.stdin.readline

def solution(N, c):
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]
    answer = -1e9

    def inboard(nrow, ncol):
        return (0 <= nrow < N) and (0 <= ncol < N)

    def valid(row, col, nrow, ncol):
        return inboard(nrow, ncol) and (c[row][col] != c[nrow][ncol])

    def action():
        row_cnt = col_cnt = 1
        row_max = col_max = -1e9
        for ro in range(N):
            for co in range(N - 1):
                if c[ro][co] == c[ro][co + 1]:
                    row_cnt += 1
                else:
                    row_cnt = 1
                row_max = max(row_max, row_cnt)
            row_cnt = 1
        for co in range(N):
            for ro in range(N - 1):
                if c[ro][co] == c[ro + 1][co]:
                    col_cnt += 1
                else:
                    col_cnt = 1
                col_max = max(col_max, col_cnt)
            col_cnt = 1

        return max(row_max, col_max)


    for row in range(N):
        for col in range(N):
            for d in range(4):
                nrow = row + drow[d]
                ncol = col + dcol[d]
                if not valid(row, col, nrow, ncol):
                    continue
                c[row][col], c[nrow][ncol] = c[nrow][ncol], c[row][col]
                answer = max(answer, action())
                c[nrow][ncol], c[row][col] = c[row][col], c[nrow][ncol]

    return answer

N = int(input().rstrip())
c = [list(input().rstrip()) for _ in range(N)]
print(solution(N, c))
