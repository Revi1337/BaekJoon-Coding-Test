import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def solution(M, N, E):

    def find(n):
        if n == parents[n]:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2)
        if root2 > root1:
            parents[root2] = root1
        else:
            parents[root1] = root2

    N, M = M, N
    tot, ans, parents = 0, 0, list(range(N + 1))
    E.sort(key = lambda x: x[2])
    for v1, v2, cost in E:
        tot += cost
        if find(v1) != find(v2):
            union(v1, v2)
            ans += cost

    return tot - ans

while True:
    M, N = map(int, input().rstrip().split())
    if M == 0 and N == 0:
        break
    E = [list(map(int, input().rstrip().split())) for _ in range(N)]
    print(solution(M, N, E))
