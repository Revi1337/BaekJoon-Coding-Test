drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]
def solution(idx, N):
    check = [[0] * N for _ in range(N)]
    row, col, cnt, d = 0, 0, 1, 0
    check[row][col] = cnt
    cnt += 1
    while cnt <= N ** 2:
        nrow = row + drow[d]
        ncol = col + dcol[d]
        if (0 <= nrow < N) and (0 <= ncol < N) and (not check[nrow][ncol]):
            row, col = nrow, ncol
            check[nrow][ncol] = cnt
            cnt += 1
        else:
            d = (d + 1) % 4
    print(f'#{idx}')
    for line in check:
        print(*line)

T = int(input())
for idx in range(T):
    N = int(input())
    solution(idx + 1, N)