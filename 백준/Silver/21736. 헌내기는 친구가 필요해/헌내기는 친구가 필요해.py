import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    srow = scol = None
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 'I':
                srow, scol = row, col
                break

    arr[srow][scol] = 'X'
    stack = [[srow, scol]]

    ans = 0
    while stack:
        row, col = stack.pop()
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if not inside(nrow, ncol) or arr[nrow][ncol] == 'X':
                continue
            if arr[nrow][ncol] in ['O', 'P']:
                if arr[nrow][ncol] == 'P':
                    ans += 1
                arr[nrow][ncol] = 'X'
                stack.append([nrow, ncol])

    return ans if ans else 'TT'

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
print(solution(N, M, arr))