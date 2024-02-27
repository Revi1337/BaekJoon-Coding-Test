import sys

sys.setrecursionlimit(10 ** 5)

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(n, colors):

    def dfs(row, col, color, dead_color):
        check[row][col] = 1
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < n) and (0 <= ncol < n) and (not check[nrow][ncol]):
                if not dead_color:
                    if colors[nrow][ncol] == color:
                        dfs(nrow, ncol, color, dead_color)
                else:
                    if (color in ['R', 'G']) and (colors[nrow][ncol] in ['R', 'G']):
                        dfs(nrow, ncol, color, dead_color)
                    elif (color == 'B') and (colors[nrow][ncol] == color):
                        dfs(nrow, ncol, color, dead_color)

    answer = [0] * 2
    for dead_color in range(2):
        check = [[0] * n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                if not check[row][col]:
                    answer[dead_color] += 1
                    dfs(row, col, colors[row][col], dead_color)

    return " ".join(map(str, answer))
n = int(input())
colors = [list(input()) for _ in range(n)]
print(solution(n, colors))