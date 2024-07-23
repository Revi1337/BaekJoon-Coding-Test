import sys
from collections import deque

input = sys.stdin.readline

def solution(N, M, V, edges):
    graphs = [[] for _ in range(N + 1)]
    for v1, v2 in edges:
        graphs[v1].append(v2)
        graphs[v2].append(v1)

    for line in graphs:
        line.sort()

    def dfs(entry):
        print(entry, end = ' ')
        check[entry] = 1
        for nv in graphs[entry]:
            if not check[nv]:
                dfs(nv)

    def bfs(entry):
        queue = deque([entry])
        check[entry] = 1
        while queue:
            v1 = queue.popleft()
            print(v1, end = ' ')
            for nv in graphs[v1]:
                if not check[nv]:
                    queue.append(nv)
                    check[nv] = 1

    check = [0] * (N + 1)
    dfs(V)
    print()
    check = [0] * (N + 1)
    bfs(V)



N, M, V = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, V, edges)
