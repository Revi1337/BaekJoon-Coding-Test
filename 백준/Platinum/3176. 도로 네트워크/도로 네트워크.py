import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

LOG = 17

def solution(N, E, K, T):

    def make_tree(n, d):
        depths[n] = d
        for nn, w in graph[n]:
            if not parents[nn][0]:
                parents[nn][0] = n
                mns[nn][0] = w
                mxs[nn][0] = w
                make_tree(nn, d + 1)

    def query(a, b):
        mn = INF
        mx = 0
        if depths[a] < depths[b]:
            a, b = b, a

        diff = depths[a] - depths[b]
        for k in range(LOG):
            if diff & (1 << k):
                mn = min(mn, mns[a][k])
                mx = max(mx, mxs[a][k])
                a = parents[a][k]

        if a == b:
            return mn, mx

        for k in range(LOG - 1, -1, -1):
            if parents[a][k] != parents[b][k]:
                mn = min(mn, mns[a][k], mns[b][k])
                mx = max(mx, mxs[a][k], mxs[b][k])
                a = parents[a][k]
                b = parents[b][k]

        mn = min(mn, mns[a][0], mns[b][0])
        mx = max(mx, mxs[a][0], mxs[b][0])

        return mn, mx

    ref = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for v1, v2, size in E:
        graph[v1].append([v2, size])
        graph[v2].append([v1, size])
        ref[v1] += 1
        ref[v2] += 1

    INF = 10 ** 15
    root = ref.index(min(ref[1:]))
    depths = [0] * (N + 1)
    parents = [[0] * LOG for _ in range(N + 1)]
    mns = [[INF] * LOG for _ in range(N + 1)]
    mxs = [[0] * LOG for _ in range(N + 1)]

    parents[root][0] = root
    mns[root][0] = INF
    mxs[root][0] = 0
    make_tree(root, 0)

    for k in range(1, LOG):
        for v in range(1, N + 1):
            # parents[n][off] = parents[parents[n][off - 1]][off - 1]
            p = parents[v][k - 1]
            parents[v][k] = parents[p][k - 1]
            mns[v][k] = min(mns[v][k - 1], mns[p][k - 1])
            mxs[v][k] = max(mxs[v][k - 1], mxs[p][k - 1])

    for a, b in T:
        print(*query(a, b))

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
K = int(input())
T = [list(map(int, input().split())) for _ in range(K)]
solution(N, E, K, T)