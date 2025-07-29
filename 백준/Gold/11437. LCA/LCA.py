import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

LOG = 17

def solution(N, E, M, Q):

    def build_tree(n, pn):
        P[0][n] = pn
        for nn in tree[n]:
            if nn != pn:
                D[nn] = D[n] + 1
                build_tree(nn, n)

    def lca(v1, v2):
        if D[v1] < D[v2]:
            v1, v2 = v2, v1
        for k in reversed(range(LOG)):
            if P[k][v1] != -1 and D[P[k][v1]] >= D[v2]:
                v1 = P[k][v1]
        if v1 == v2:
            return v1
        for k in reversed(range(LOG)):
            if P[k][v1] != -1 and P[k][v1] != P[k][v2]:
                v1 = P[k][v1]
                v2 = P[k][v2]
        return P[0][v1]

    tree = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        tree[v1].append(v2)
        tree[v2].append(v1)

    D = [0] * (N + 1)
    P = [[-1] * (N + 1) for _ in range(LOG)]
    build_tree(1, -1)

    for idx in range(1, LOG):
        for jdx in range(1, N + 1):
            if P[idx - 1][jdx] != -1:
                P[idx][jdx] = P[idx - 1][P[idx - 1][jdx]]

    for v1, v2 in Q:
        print(lca(v1, v2))


N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
M = int(input())
Q = [list(map(int, input().split())) for _ in range(M)]
solution(N, E, M, Q)