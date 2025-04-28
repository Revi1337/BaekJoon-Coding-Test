import sys

sys.setrecursionlimit(10 ** 5)

def solution(N, M, edges):

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        aroot = find(a)
        broot = find(b)
        if aroot == broot:
            return False

        if rank[aroot] < rank[broot]:
            parent[aroot] = broot
        else:
            parent[broot] = aroot
            if rank[aroot] == rank[broot]:
                rank[aroot] += 1
        return True

    parent = [i for i in range(N)]
    rank = [0 for _ in range(N)]
    for seq, (v1, v2) in enumerate(edges, start=1):
        if not union(v1, v2):
            return seq
    return 0

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, edges))
