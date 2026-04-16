# 2026-04-16
# https://www.acmicpc.net/problem/1987
# V4. bfs + set check

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(R, C, arr):

    inside = lambda row, col : 0 <= row < R and 0 <= col < C

    check = [[set() for _ in range(C)] for _ in range(R)]
    check[0][0].add(arr[0][0])
    ans, queue = 1, deque([[0, 0, arr[0][0]]])

    while queue:
        row, col, char = queue.popleft()
        ans = max(ans, len(char))
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if not inside(nrow, ncol):
                continue
            if arr[nrow][ncol] in char:
                continue
            if char + arr[nrow][ncol] in check[nrow][ncol]:
                continue
            check[nrow][ncol].add(char + arr[nrow][ncol])
            queue.append([nrow, ncol, char + arr[nrow][ncol]])

    return ans

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
print(solution(R, C, arr))