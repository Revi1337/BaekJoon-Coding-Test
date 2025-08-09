import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, arr):

    SIZE = N ** 2
    inside = lambda row, col : 0 <= row < N and 0 <= col < N

    ans = 200 * (10 ** 2)
    for p1 in range(SIZE):
        for p2 in range(p1 + 1, SIZE):
            for p3 in range(p2 + 1, SIZE):
                check = [[0] * (N + 1) for _ in range(N + 1)]
                sm, possible = 0, True
                for p in p1, p2, p3:
                    row, col = p // N, p % N
                    if check[row][col]:
                        possible = False
                        break
                    check[row][col] = 1
                    sm += arr[row][col]
                    for d in range(4):
                        nrow, ncol = row + drow[d], col + dcol[d]
                        if not inside(nrow, ncol) or check[nrow][ncol]:
                            possible = False
                            break
                        check[nrow][ncol] = 1
                        sm += arr[nrow][ncol]
                if possible:
                    ans = min(ans, sm)

    return ans

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))

