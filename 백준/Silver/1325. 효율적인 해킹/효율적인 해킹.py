from collections import deque

def solution(N, M, E):

    graph = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        graph[v2].append(v1)

    dist, mx = [0] * (N + 1), 0
    for n in range(1, N + 1):
        check, ans = [0] * (N + 1), 0
        check[n] = 1
        queue = deque([n])
        while queue:
            nn = queue.popleft()
            ans += 1
            for nnn in graph[nn]:
                if not check[nnn]:
                    check[nnn] = 1
                    queue.append(nnn)

        dist[n] = ans
        mx = max(mx, dist[n])

    print(*[n for n in range(1, N + 1) if dist[n] == mx], sep = ' ')

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, E)
