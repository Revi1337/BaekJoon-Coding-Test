# 2026-04-25
# https://www.acmicpc.net/problem/1967
# 트리의 지름
# tree
# bfs (임의의 정점에서 출발하여 가장 먼(가중치기반) 노드를 찾고, 찾은 노드에서 가장 먼 노드를 구한다)

from collections import deque

def solution(N, E):

    tree = [[] for _ in range(N + 1)]
    for v1, v2, c in E:
        tree[v1].append([v2, c])
        tree[v2].append([v1, c])

    mx, mxn = 0, 1
    queue = deque([(1, 1, 0)])
    while queue:
        cn, pn, c = queue.popleft()
        if c > mx:
            mx, mxn = c, cn
        for nn, nc in tree[cn]:
            if nn != pn:
                queue.append((nn, cn, c + nc))

    ans = 0
    queue = deque([(mxn, mxn, 0)])
    while queue:
        cn, pn, c = queue.popleft()
        ans = max(ans, c)
        for nn, nc in tree[cn]:
            if nn != pn:
                queue.append((nn, cn, c + nc))

    return ans

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
print(solution(N, E))
