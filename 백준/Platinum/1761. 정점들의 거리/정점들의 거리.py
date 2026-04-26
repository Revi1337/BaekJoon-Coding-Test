# 2026-04-26
# https://www.acmicpc.net/problem/1761
# 정점들의 거리
# tree

import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit((10 ** 4) * 5)

LOG = math.ceil(math.log2(40_000))

def solution(N, E, M, Q):

    def find_root():
        freq = [0] * (N + 1)
        for v1, v2, c in E:
            freq[v1] += 1
            freq[v2] += 1

        return freq.index(min(freq[1:]))

    def make_tree(n, pn, d, sm):
        parents[n][0] = pn
        depth[n] = d
        dist[n] = sm
        for nn, nc in tree[n]:
            if nn != pn:
                make_tree(nn, n, d + 1, sm + nc)

    def binary_lift():
        for k in range(1, LOG):
            for n in range(1, N + 1):
                parents[n][k] = parents[parents[n][k - 1]][k - 1]

    def lca(n1, n2):
        cn1, cn2 = n1, n2
        if depth[n1] > depth[n2]:
            n1, n2, cn1, cn2 = n2, n1, cn2, cn1
        for k in range(LOG - 1, -1, -1):
            if depth[n2] - depth[n1] >= (1 << k):
                n2 = parents[n2][k]
        if n1 == n2:
            return dist[cn2] - dist[cn1]
        for k in range(LOG - 1, -1, -1):
            if parents[n1][k] != parents[n2][k]:
                n1, n2 = parents[n1][k], parents[n2][k]
        return (dist[cn2] - dist[parents[n1][0]]) + (dist[cn1] - dist[parents[n1][0]])

    tree = [[] for _ in range(N + 1)]
    for v1, v2, c in E:
        tree[v1].append([v2, c])
        tree[v2].append([v1, c])

    depth, dist = [[0] * (N + 1) for _ in range(2)]
    parents = [[0] * LOG for _ in range(N + 1)]
    root = find_root()

    make_tree(root, root, 0, 0)
    binary_lift()

    for ns in Q:
        print(lca(*ns))

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
M = int(input())
Q = [list(map(int, input().split())) for _ in range(M)]
solution(N, E, M, Q)
