# 2026-04-26
# https://www.acmicpc.net/problem/1167
# 트리의 지름
# tree

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit((10 ** 5) * 2)

def solution(V, E):

    tree = [[] for _ in range(V + 1)]
    for entry in E:
        v1 = entry[0]
        for idx in range(1, len(entry) - 1, 2):
            v2, c = entry[idx], entry[idx + 1]
            tree[v1].append([v2, c])

    def dfs(n, pn, d):
        mn, mc = n, d
        for nn, nc in tree[n]:
            if nn != pn:
                cn, cc = dfs(nn, n, d + nc)
                if cc > mc:
                    mn, mc = cn, cc

        return mn, mc

    mxn, _ = dfs(1, 1, 0)

    ans = 0
    queue = deque([(mxn, mxn, 0)])
    while queue:
        n, pn, cost = queue.popleft()
        ans = max(ans, cost)
        for nn, nc in tree[n]:
            if nn != pn:
                queue.append((nn, n, cost + nc))

    return ans

V = int(input())
E = [list(map(int, input().split())) for _ in range(V)]
print(solution(V, E))
