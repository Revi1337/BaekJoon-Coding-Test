# 2026-04-16
# https://www.acmicpc.net/problem/1987
# 알파벳 (백트래킹 + 비트마스킹) bfs 로도 가능할듯?
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    def backtrack(srow, scol, check, cnt):
        nonlocal ans
        ans = max(ans, cnt)
        if ans == 26:
            return
        for d in range(4):
            nrow, ncol = srow + drow[d], scol + dcol[d]
            if inside(nrow, ncol):
                bit = 1 << (ord(arr[nrow][ncol]) - 65)
                if not (check & bit):
                    backtrack(nrow, ncol, check | bit, cnt + 1)

    ans = 0
    start = 1 << (ord(arr[0][0]) - 65)
    backtrack(0, 0, start, 1)
    return ans

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
print(solution(N, M, arr))