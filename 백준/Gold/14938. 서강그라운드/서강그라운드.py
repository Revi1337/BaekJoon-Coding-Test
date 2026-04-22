# 2026-04-22
# https://www.acmicpc.net/problem/14938
# 서강그라운드
# V1. Floyd-Warshall

def solution(N, M, R, T, E):
    T.insert(0, 0)

    INF = float('inf')
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for n in range(1, N + 1):
        dist[n][n] = 0

    for a, b, l in E:
        dist[a][b] = min(dist[a][b], l)
        dist[b][a] = min(dist[b][a], l)

    for mid in range(1, N + 1):
        for st in range(1, N + 1):
            for end in range(1, N + 1):
                if dist[st][end] > dist[st][mid] + dist[mid][end]:
                    dist[st][end] = dist[st][mid] + dist[mid][end]

    ans = 0
    for st in range(1, N + 1):
        sm = 0
        for end in range(1, N + 1):
            if dist[st][end] <= M:
                sm += T[end]
        ans = max(ans, sm)

    return ans

N, M, R = map(int, input().split())
T = list(map(int, input().split()))
E = [list(map(int, input().split())) for _ in range(R)]
print(solution(N, M, R, T, E))