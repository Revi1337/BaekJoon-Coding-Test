# 2026-04-24
# https://www.acmicpc.net/problem/11657
# 타임머신
# bellman-ford

def solution(N, M, E):
    INF = float('inf')
    dist = [INF] * (N + 1)

    dist[1] = 0
    for n in range(N):
        for v1, v2, c in E:
            if dist[v1] + c < dist[v2]:
                dist[v2] = dist[v1] + c
                if n == N - 1:
                    print(-1)
                    return

    print(*[c if c != INF else -1 for c in dist[2:]], sep='\n')

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, E)