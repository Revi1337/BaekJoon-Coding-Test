drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, row, col, sd, arr):
    ans = 0
    while True:
        if not arr[row][col]:
            ans += 1
            arr[row][col] = 2

        cleaned = True
        for d in range(4):
            if not arr[row + drow[d]][col + dcol[d]]:
                cleaned = False
                break

        if cleaned:
            row, col = row + drow[sd] * -1, col + dcol[sd] * -1
            if arr[row][col] == 1:
                return ans
        else:
            sd = (sd - 1) % 4
            if arr[row + drow[sd]][col + dcol[sd]] == 0:
                row, col = row + drow[sd], col + dcol[sd]

N, M = map(int, input().split())
row, col, sd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, row, col, sd, arr))