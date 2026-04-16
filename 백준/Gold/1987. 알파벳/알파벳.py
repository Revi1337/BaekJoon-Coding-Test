# 2026-04-16
# https://www.acmicpc.net/problem/1987
# 알파벳 (백트래킹) bfs 로도 가능할듯?

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    def backtrack(srow, scol, check, cnt):
        nonlocal ans
        ans = max(ans, cnt)
        for d in range(4):
            nrow, ncol = srow + drow[d], scol + dcol[d]
            if inside(nrow, ncol):
                sign = arr[nrow][ncol]
                if sign not in check:
                    check.add(sign)
                    backtrack(nrow, ncol, check, cnt + 1)
                    check.discard(sign)

    ans = 0
    backtrack(0, 0, set(arr[0][0]), 1)

    return ans

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
print(solution(N, M, arr))