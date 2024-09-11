import sys

input = sys.stdin.readline

"""
알파벳 (https://www.acmicpc.net/problem/1987)
2024-09-11
"""

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(R, C, boards):

    def dfs(row, col):
        nonlocal answer
        answer = max(answer, len(cache))
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if 0 <= nrow < R and 0 <= ncol < C and boards[nrow][ncol] not in cache:
                cache.add(boards[nrow][ncol])
                dfs(nrow, ncol)
                cache.discard(boards[nrow][ncol])

    answer = 1
    cache = set(boards[0][0])
    dfs(0, 0)

    return answer

R, C = map(int, input().split())
boards = [list(input().rstrip()) for _ in range(R)]
print(solution(R, C, boards))
