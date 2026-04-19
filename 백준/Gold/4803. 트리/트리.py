# 2026-04-19
# https://www.acmicpc.net/problem/4803
# 트리

def solution(seq, N, M, E):

    def find(n):
        while n != parents[n]:
            parents[n] = parents[parents[n]]
            n = parents[n]
        return n

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if r1 < r2:
            parents[r2] = r1
        else:
            parents[r1] = r2

    parents = list(range(N + 1))
    cyc = set()
    for n1, n2 in E:
        if find(n1) != find(n2):
            union(n1, n2)
        else:
            cyc.add(n1)
            cyc.add(n2)

    parents = [find(n) for n in range(N + 1)]
    cyc_root = set(parents[cn] for cn in cyc)

    ans = len(set(parents[1:]) - cyc_root)
    if not ans:
        return f'Case {seq}: No trees.'
    return f'Case {seq}: There is one tree.' if ans == 1 else f'Case {seq}: A forest of {ans} trees.'

seq = 1
while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    E = [list(map(int, input().split())) for _ in range(M)]
    print(solution(seq, N, M, E))
    seq += 1