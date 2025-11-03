# 2025-11-04
# https://www.acmicpc.net/problem/11438

import sys
import math

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

LOG = math.ceil(math.log2(100_000))

def solution(N, E, M, Q):

    def make_tree(n, pn, d):
        depths[n] = d
        parents[n][0] = pn
        for nn in tree[n]:
            if nn != pn:
                make_tree(nn, n, d + 1)

    def lca(n1, n2):
        if depths[n1] > depths[n2]:
            n1, n2 = n2, n1
        for idx in range(LOG - 1, -1, -1):
            if depths[n2] - depths[n1] >= (1 << idx):
                n2 = parents[n2][idx]
        if n1 == n2:
            return n1
        for idx in range(LOG - 1, -1, -1):
            if parents[n1][idx] != parents[n2][idx]:
                n1, n2 = parents[n1][idx], parents[n2][idx]
        return parents[n1][0]

    tree = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        tree[v1].append(v2)
        tree[v2].append(v1)

    depths = [0] * (N + 1)
    parents = [[0] * LOG for _ in range(N + 1)]
    make_tree(1, 1, 0)

    for off in range(1, LOG):
        for n in range(1, N + 1):
            parents[n][off] = parents[parents[n][off - 1]][off - 1]

    for n1, n2 in Q:
        print(lca(n1, n2))

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
M = int(input())
Q = [list(map(int, input().split())) for _ in range(M)]
solution(N, E, M, Q)