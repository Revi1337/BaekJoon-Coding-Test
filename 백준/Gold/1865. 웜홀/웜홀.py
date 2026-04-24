# 2026-04-24
# https://www.acmicpc.net/problem/1865
# 웜홀
# bellman-ford

def solution(N, M, W, E, WW):
    EE = []
    for v1, v2, c in E:
        EE.append((v1, v2, c))
        EE.append((v2, v1, c))
    for v1, v2, c in WW:
        EE.append((v1, v2, -c))

    for v in range(1, N + 1):
        EE.append((0, v, 0))

    dist = [0] * (N + 1)
    st = 0
    dist[st] = 0
    for v in range(N):
        for v1, v2, c in EE:
            if dist[v1] + c < dist[v2]:
                dist[v2] = dist[v1] + c
                if v == N - 1:
                    return 'YES'
    return 'NO'

T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    E = [list(map(int, input().split())) for _ in range(M)]
    WW = [list(map(int, input().split())) for _ in range(W)]
    print(solution(N, M, W, E, WW))