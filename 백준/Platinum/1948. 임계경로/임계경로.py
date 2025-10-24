import sys
from collections import deque

input = sys.stdin.readline

def solution(N, M, E, ST, END):
    graph = [[] for _ in range(N + 1)]
    ind = [0] * (N + 1)
    for v1, v2, pt in E:
        graph[v1].append([v2, pt])
        ind[v2] += 1

    dist = [0] * (N + 1)
    queue = deque([ST])
    while queue:
        n = queue.popleft()
        for nn, nt in graph[n]:
            if dist[nn] < dist[n] + nt:
                dist[nn] = dist[n] + nt
            ind[nn] -= 1
            if ind[nn] == 0:
                queue.append(nn)

    rgraph = [[] for _ in range(N + 1)]
    for v1, v2, t in E:
        rgraph[v2].append([v1, t])

    queue = deque([END])
    cnt, check = 0, [0] * (N + 1)
    check[END] = 1
    while queue:
        n = queue.popleft()
        for pn, pt in rgraph[n]:
            if dist[pn] + pt == dist[n]:
                cnt += 1
                if not check[pn]:
                    check[pn] = 1
                    queue.append(pn)

    print(dist[END], cnt, sep='\n')

N = int(input())
M = int(input())
E = [list(map(int, input().split())) for _ in range(M)]
ST, END = map(int, input().split())
solution(N, M, E, ST, END)