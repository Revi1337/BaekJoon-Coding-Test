import sys

sys.setrecursionlimit(10 ** 5 + 30)

def solution(N, E):

    def make_tree(n, p):
        parents[n] = p
        for nn in tree[n]:
            if nn != p:
                make_tree(nn, n)

    tree = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        tree[v1].append(v2)
        tree[v2].append(v1)

    parents = [0] * (N + 1)
    parents[1] = -1
    make_tree(1, -1)

    print(*parents[2:], end = '\n')

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
solution(N, E)