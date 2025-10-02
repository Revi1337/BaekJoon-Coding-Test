# 2025-10-02
# https://www.acmicpc.net/problem/1774

import sys
from math import sqrt

input = sys.stdin.readline

def solution(N, M, E, C):

    def find(n):
        if n == parents[n]:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2)
        if root2 > root1:
            parents[root2] = root1
        else:
            parents[root1] = root2

    E.insert(0, [0, 0])
    edges = []
    for e1 in range(1, N + 1):
        for e2 in range(N):
            if e1 != e2:
                row1, col1 = E[e1]
                row2, col2 = E[e2]
                edges.append((e1, e2, sqrt(pow(row1 - row2, 2) + pow(col1 - col2, 2))))

    edges.sort(key=lambda pos: pos[2])
    parents = list(range(N + 1))
    for v1, v2 in C:
        if find(v1) != find(v2):
            union(v1, v2)

    cnt = ans = 0
    for v1, v2, c in edges:
        if v1 and v2 and find(v1) != find(v2):
            union(v1, v2)
            ans += c
            cnt += 1

    return "{:.2f}".format(ans)

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(N)]
C = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, E, C))