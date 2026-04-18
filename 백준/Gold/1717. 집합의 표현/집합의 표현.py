# 2026-04-18
# https://www.acmicpc.net/problem/1717
# 집합의 표현
# Union-Find

import sys

sys.setrecursionlimit(10 ** 7)

def solution(N, M, E):

    def find(n):
        if n == parents[n]:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if r1 < r2:
            parents[r2] = r1
        else:
            parents[r1] = r2

    parents = list(range(N + 1))
    for op, n1, n2 in E:
        if not op:
            union(n1, n2)
        else:
            if find(n1) == find(n2):
                print('YES')
            else:
                print('NO')

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, E)