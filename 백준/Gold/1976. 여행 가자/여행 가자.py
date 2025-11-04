import sys

input = sys.stdin.readline

def solution(N, M, E, T):

    def find(n):
        if n == parents[n]:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2),
        if root1 < root2:
            parents[root2] = root1
        else:
            parents[root1] = root2

    parents = list(range(N + 1))
    for n, ns in enumerate(E, start=1):
        for nn in range(len(ns)):
            if ns[nn] and find(n) != find(nn + 1):
                union(n, nn + 1)

    for n in range(1, N + 1):
        find(n)

    return 'YES' if len(set(parents[t] for t in T)) == 1 else 'NO'

N = int(input())
M = int(input())
E = [list(map(int, input().split())) for _ in range(N)]
T = list(map(int, input().split()))
print(solution(N, M, E, T))
