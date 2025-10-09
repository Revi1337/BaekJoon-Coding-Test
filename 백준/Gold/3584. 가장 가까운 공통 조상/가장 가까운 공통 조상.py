import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def solution(N, E, V1, V2):

    def make_tree(n, pn, lv):
        lvs[n] = lv
        for nn in tree[n]:
            if nn != pn:
                make_tree(nn, n, lv + 1)

    tree = [[] for _ in range(N + 1)]
    refers, parents = [[0] * (N + 1) for _ in range(2)]
    for v1, v2 in E:
        tree[v1].append(v2)
        parents[v2] = v1
        refers[v2] += 1

    root, lvs = refers[1:].index(min(refers[1:])) + 1, [0] * (N + 1)
    make_tree(root, -1, 0)

    mxn = V1 if lvs[V1] >= lvs[V2] else V2
    mnn = V2 if mxn == V1 else V1
    diff = abs(lvs[V1] - lvs[V2])

    while diff > 0:
        mxn = parents[mxn]
        diff -= 1

    while mxn != mnn:
        mxn, mnn = parents[mxn], parents[mnn]

    return mxn

T = int(input())
for _ in range(T):
    N = int(input())
    E = [list(map(int, input().split())) for _ in range(N - 1)]
    V1, V2 = map(int, input().split())
    print(solution(N, E, V1, V2))

