import sys

input = sys.stdin.readline

"""
알파벳 (https://www.acmicpc.net/problem/1987)
2024-09-11
"""

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution2(R, C, boards):

    def dfs(row, col, counter):
        nonlocal answer
        answer = max(answer, counter)
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if 0 <= nrow < R and 0 <= ncol < C:
                if cache[(65 - ord(boards[nrow][ncol])) % 26] == 0:
                    cache[(65 - ord(boards[nrow][ncol])) % 26] = 1
                    dfs(nrow, ncol, counter + 1)
                    cache[(65 - ord(boards[nrow][ncol])) % 26] = 0

    answer = 1
    cache = [0] * 26
    cache[(65 - ord(boards[0][0])) % 26] = 1
    dfs(0, 0, 1)

    return answer

R, C = map(int, input().split())
boards = [list(input().rstrip()) for _ in range(R)]
print(solution2(R, C, boards))
