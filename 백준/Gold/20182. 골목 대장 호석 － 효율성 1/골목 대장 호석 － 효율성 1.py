# 2026-04-23
# https://www.acmicpc.net/problem/20182
# 골목 대장 호석 - 효율성 1
# binary-search + dijkstra
# 상당히 좋은 문제인듯?

import heapq

def solution(N, M, A, B, C, E):

    INF = float('inf')

    def possible(lim):
        """base on dijkstra"""
        dist = [INF] * (N + 1)
        dist[A] = 0
        pq = [[dist[A], A]]

        while pq:
            c, n = heapq.heappop(pq)
            if c > dist[n]:
                continue
            if n == B:
                return dist[B] if dist[B] <= C else None
            for nn, nc in graph[n]:
                if c + nc < dist[nn] and nc <= lim:
                    dist[nn] = c + nc
                    heapq.heappush(pq, [dist[nn], nn])
        return None

    graph = [[] for _ in range(N + 1)]
    arr = []
    for v1, v2, c in E:
        graph[v1].append([v2, c])
        graph[v2].append([v1, c])
        arr.append(c)

    arr.sort()
    ans, left, right = INF, 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if possible(arr[mid]):
            ans = min(ans, arr[mid])
            right = mid - 1
        else:
            left = mid + 1

    return ans if ans != INF else -1

N, M, A, B, C = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, A, B, C, E))