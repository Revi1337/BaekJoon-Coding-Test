# 2026-04-20
# https://www.acmicpc.net/problem/1939
# 중량제한
# V2. Binary Search + 최대힙(Dijkstra는 아님)

import heapq

def solution(N, M, E, arr):

    st, end = arr

    def possible(lim):
        check = [0] * (N + 1)
        check[st] = 1
        pq = [[0, st]]
        while pq:
            _, n = heapq.heappop(pq)
            if n == end:
                return True
            for nn, nl in graph[n]:
                if not check[nn] and nl >= lim:
                    check[nn] = 1
                    heapq.heappush(pq, [-nl, nn])
        return False

    graph = [[] for _ in range(N + 1)]
    for v1, v2, lim in E:
        graph[v1].append([v2, lim])
        graph[v2].append([v1, lim])

    left, right = 1, 1_000_000_000
    while left <= right:
        mid = (left + right) // 2
        if possible(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
arr = list(map(int, input().split()))
print(solution(N, M, E, arr))