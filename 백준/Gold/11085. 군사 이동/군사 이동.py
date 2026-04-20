# 2026-04-19
# https://www.acmicpc.net/problem/11085
# 군사 이동
# V1. Binary Search + BFS

from collections import deque

def solution(P, W, start, end, E):

    def possible(limit):
        check = [0] * P
        queue = deque([start])
        check[start] = 1

        while queue:
            n = queue.popleft()
            if n == end:
                return True
            for nn, w in graph[n]:
                if not check[nn] and w >= limit:
                    check[nn] = True
                    queue.append(nn)
        return False

    graph = [[] for _ in range(P)]
    for a, b, w in E:
        graph[a].append((b, w))
        graph[b].append((a, w))

    left, right = 1, 1000
    while left <= right:
        mid = (left + right) // 2
        if possible(mid):
            left = mid + 1
        else:
            right = mid - 1

    return left - 1

P, W = map(int, input().split())
C, V = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(W)]
print(solution(P, W, C, V, E))