import sys

input = sys.stdin.readline

def solution(N, M, K, C, E):

    def find(n):
        if n == parents[n]:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2)
        if root1 < root2:
            parents[root2] = root1
        else:
            parents[root1] = root2

    parents = list(range(N + 1))
    for v1, v2 in E:
        if find(v1) != find(v2):
            union(v1, v2)

    for n in range(1, N + 1):
        find(n)

    counter = dict()
    for n, pn in enumerate(parents[1:], start=1):
        counter[pn] = counter.get(pn, [])
        counter[pn].append(n)

    ans = sum([min(map(lambda n: C[n - 1], lst)) for key, lst in counter.items()])
    return 'Oh no' if ans > K else ans

N, M, K = map(int, input().split())
C = list(map(int, input().split()))
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, K, C, E))