import sys
import heapq

input = sys.stdin.readline

def solution(N, M, S, E):
    S.insert(0, 0)
    graph = [[] for _ in range(N + 1)]
    for v1, v2, cost in E:
        graph[v1].append([v2, cost])
        graph[v2].append([v1, cost])

    st = 1
    check = [0] * (N + 1)
    pq = [[0, st, -1]]
    mst = []

    while pq:
        c, n, pn = heapq.heappop(pq)
        if check[n]:
            continue
        check[n] = 1
        if pn != -1:
            mst.append([pn, c, n])
        for nn, nc in graph[n]:
            if S[nn] != S[n]:
                heapq.heappush(pq, [nc, nn, n])

    return sum(c for _, c, _ in mst) if sum(check[1:]) == N else -1

N, M = map(int, input().split())
S = input().rstrip().split()
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, S, E))
