# 2026-04-19
# https://www.acmicpc.net/problem/1939
# 중량제한
# V1. Binary Search + BFS

from collections import deque

def solution(N, M, E, arr):

    st, end = arr

    def possible(lim):
        check = [0] * (N + 1)
        check[st] = 1
        queue = deque([st])
        while queue:
            n = queue.popleft()
            if n == end:
                return True
            for nn, nlim in graph[n]:
                if nlim >= lim and not check[nn]:
                    check[nn] = 1
                    queue.append(nn)
        return False

    graph = [[] for _ in range(N + 1)]
    for v1, v2, lim in E:
        graph[v1].append([v2, lim])
        graph[v2].append([v1, lim])

    for ns in graph:
        ns.sort(key=lambda x: x[1])

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

