def solution(N, edges):

    def find(n):
        if island[n] == n:
            return n

        island[n] = find(island[n])
        return island[n]

    def union(i1, i2):
        r1, r2 = find(i1), find(i2)
        if r1 < r2:
            island[r2] = r1
        else:
            island[r1] = r2

    island = list(range(0, N + 1))
    for i1, i2 in edges:
        union(i1, i2)

    init = find(1)
    for land in range(2, N + 1):
        if init != find(land):
            print(1, land)
            return

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N - 2)]
solution(N, edges)