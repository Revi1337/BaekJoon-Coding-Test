drow = [-2, 0, 2, 0]
dcol = [0, 2, 0, -2]

def solution(N, K, towers):
    check = {(row - 1, col - 1) for row, col in towers}
    for row, col in towers:
        row, col = row - 1, col - 1
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if 0 <= nrow < N and 0 <= ncol < N and (nrow, ncol) not in check:
                check.add((nrow, ncol))

    return len(check) - K

N, K = map(int, input().split())
towers = [list(map(int, input().split())) for _ in range(K)]
print(solution(N, K, towers))
