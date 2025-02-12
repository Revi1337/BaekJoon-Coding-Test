import sys

sys.setrecursionlimit(10**6)

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(M, N, roads):
    roads.insert(0, [0] * (N + 2))
    for idx in range(1, M + 1):
        roads[idx] = [0] + roads[idx] + [0]
    roads.append([0] * (N + 2))

    def dfs(srow, scol):
        if dp[srow][scol] == -1:
            dp[srow][scol] = 0
            for d in range(4):
                prow, pcol = srow + drow[d], scol + dcol[d]
                if roads[prow][pcol] > roads[srow][scol]:
                    dp[srow][scol] += dfs(prow, pcol)
        return dp[srow][scol]

    dp = [[-1] * (N + 2) for _ in range(M + 2)]
    dp[1][1] = 1

    return dfs(M, N)

M, N = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]
print(solution(M, N, roads))