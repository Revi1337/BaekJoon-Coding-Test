import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution(N, E):

    graph = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        graph[v1].append(v2)
        graph[v2].append(v1)

    dp = [[0, 1] for _ in range(N + 1)]
    check = [0] * (N + 1)

    def dfs(n):
        check[n] = 1
        for nn in graph[n]:
            if not check[nn]:
                dfs(nn)
                dp[n][0] += dp[nn][1]
                dp[n][1] += min(dp[nn][0], dp[nn][1])

    dfs(1)

    return min(dp[1][0], dp[1][1])

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
print(solution(N, E))