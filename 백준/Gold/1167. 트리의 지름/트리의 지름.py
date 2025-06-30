import sys
from collections import deque

sys.setrecursionlimit(10 ** 5)

def solution(V, arr):
    graph = [[] for _ in range(V + 1)]
    for line in arr:
        for idx in range(1, len(line) - 1, 2):
            graph[line[0]].append([line[idx], line[idx + 1]])

    def dfs(n):
        for nn, cost in graph[n]:
            if dist[nn] == -1:
                dist[nn] = dist[n] + cost
                dfs(nn)

    def bfs(n):
        check = [-1] * (V + 1)
        check[n] = mx = 0
        queue = deque([n])

        while queue:
            node = queue.popleft()
            mx = max(mx, check[node])
            for nn, cost in graph[node]:
                if check[nn] == -1:
                    check[nn] = check[node] + cost
                    queue.append(nn)
        return mx

    dist = [-1] * (V + 1)
    dist[1] = 0
    dfs(1)
    st = dist.index(max(dist))

    return bfs(st)

V = int(input())
arr = [list(map(int, input().split())) for _ in range(V)]
print(solution(V, arr))