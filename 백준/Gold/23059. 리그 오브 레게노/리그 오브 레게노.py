import sys
import heapq

input = sys.stdin.readline

def solution(N, arr):
    graph, ind = {}, {}
    for i1, i2 in arr:
        graph[i1] = graph.get(i1, [])
        graph[i2] = graph.get(i2, [])
        graph[i1].append(i2)
        ind[i1] = ind.get(i1, 0)
        ind[i2] = ind.get(i2, 0)

    for i1, i2 in arr:
        ind[i2] += 1

    pri, pq, ans = {key: 0 for key in ind}, [], []
    for i1, cnt in ind.items():
        if not cnt:
            pri[i1] = 1
            heapq.heappush(pq, i1)

    while pq:
        levels = []
        while pq:
            levels.append(heapq.heappop(pq))
        levels.sort()
        ans.extend(levels)
        for item in levels:
            for nxt in graph[item]:
                ind[nxt] -= 1
                if ind[nxt] == 0:
                    heapq.heappush(pq, nxt)

    if len(ans) != len(ind):
        print(-1)
    else:
        print(*ans, sep = '\n')

N = int(input())
arr = [input().rstrip().split() for _ in range(N)]
solution(N, arr)