import sys
import math

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

LOG = math.ceil(math.log2(40_000))

def solution(N, E, M, Q):

    def make_tree_and_find_root():
        ref = [0] * (N + 1)
        tree = [[] for _ in range(N + 1)]
        for v1, v2, cost in E:
            tree[v2].append([v1, cost])
            tree[v1].append([v2, cost])
            ref[v1], ref[v2] = ref[v1] + 1, ref[v2] + 1

        return tree, ref.index(min(ref[1:]))

    def tree_trav(n, pn, d):
        parents[n][0] = pn
        depths[n] = d
        for nn, nc in tree[n]:
            if nn != pn:
                dist[nn] = dist[n] + nc
                tree_trav(nn, n, d + 1)

    def set_parents():
        for k in range(1, LOG):
            for n in range(1, N + 1):
                parents[n][k] = parents[parents[n][k - 1]][k - 1]

    def lca_with_dist(n1, n2):
        cn1, cn2 = n1, n2
        if depths[n1] > depths[n2]:
            n1, n2, cn1, cn2 = n2, n1, n2, n1
        for k in range(LOG - 1, -1, -1):
            if depths[n2] - depths[n1] >= (1 << k):
                n2 = parents[n2][k]
        if n1 == n2:
            return dist[cn2] - dist[cn1]
        for k in range(LOG - 1, -1, -1):
            if parents[n1][k] != parents[n2][k]:
                n1, n2 = parents[n1][k], parents[n2][k]
        return (dist[cn1] - dist[parents[n1][0]]) + (dist[cn2] - dist[parents[n1][0]])

    parents = [[0] * LOG for _ in range(N + 1)]
    depths, dist = [[0] * (N + 1) for _ in range(2)]
    tree, root = make_tree_and_find_root()
    tree_trav(root, root, 0)
    set_parents()

    for ns in Q:
        print(lca_with_dist(*ns))

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
M = int(input())
Q = [list(map(int, input().split())) for _ in range(M)]
solution(N, E, M, Q)