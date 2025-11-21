# 2025-11-21
# https://www.acmicpc.net/problem/11085

import sys

input = sys.stdin.readline

def solution(P, W, C, V, E):

    def find(n):
        if n == parents[n]:
            return n
        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if r1 != r2:
            if r1 > r2:
                parents[r1] = r2
            else:
                parents[r2] = r1

    E.sort(key=lambda x: -x[2])
    parents = list(range(P + 1))
    for n1, n2, c in E:
        union(n1, n2)
        if find(C) == find(V):
            return c

P, W = map(int, input().split())
C, V = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(W)]
print(solution(P, W, C, V, E))

