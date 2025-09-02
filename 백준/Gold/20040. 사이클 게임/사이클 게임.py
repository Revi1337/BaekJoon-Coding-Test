import sys

input = sys.stdin.readline

def solution(N, M, E):

    def find(n):
        if n == parent[n]:
            return parent[n]

        parent[n] = find(parent[n])
        return parent[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2)
        if root1 < root2:
            parent[root2] = root1
        else:
            parent[root1] = root2

    parent = list(range(N + 1))
    for idx, (v1, v2) in enumerate(E, start=1):
        if find(v1) == find(v2):
            return idx
        union(v1, v2)

    return 0

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, E))