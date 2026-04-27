# 2026-04-27
# https://www.acmicpc.net/problem/14621
# 나만 안되는 연애
# MST
# kruskal 또는 prim

import sys

input = sys.stdin.readline

def solution(N, M, S, E):
    """ kruskal """

    def find(n):
        while n != parents[n]:
            parents[n] = parents[parents[n]]
            n = parents[n]
        return n

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if r1 < r2:
            parents[r2] = r1
        else:
            parents[r1] = r2

    S.insert(0, 0)
    E.sort(key=lambda x: x[2])
    parents = list(range(N + 1))

    ans = cnt = 0
    for n1, n2, c in E:
        if find(n1) != find(n2) and S[n1] != S[n2]:
            union(n1, n2)
            ans += c
            cnt += 1

    return ans if cnt == N - 1 else -1

N, M = map(int, input().split())
S = input().rstrip().split()
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, S, E))