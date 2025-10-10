def solution(N, M, E):

    def find(n):
        if n == parents[n]:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2)
        if root1 > root2:
            parents[root1] = root2
        else:
            parents[root2] = root1

    parents, cycle = list(range(N + 1)), set()
    for v1, v2 in E:
        if find(v1) != find(v2):
            union(v1, v2)
        else:
            cycle.add(v1)
            cycle.add(v2)

    parents = [find(n) for n in range(N + 1)]
    cycle_roots = {parents[cn] for cn in cycle}
    rlen = len({parents[n] for n in range(1, N + 1) if parents[n] not in cycle_roots})

    if not rlen:
        return 'No trees.'
    return 'There is one tree.' if rlen == 1 else f'A forest of {rlen} trees.'

idx = 1
while True:
    N, M = map(int, input().rstrip().split())
    if N == 0 and M == 0:
        break
    E = [list(map(int, input().rstrip().split())) for _ in range(M)]
    print(f'Case {idx}: {solution(N, M, E)}')
    idx += 1
