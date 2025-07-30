import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def solution(N, M, E):

    def find(n):
        if n == P[n]:
            return n

        P[n] = find(P[n])
        return P[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2)
        if root2 > root1:
            P[root2] = root1
        else:
            P[root1] = root2

    P, C = list(range(N + 1)), set()
    for n1, n2 in E:
        r1, r2 = find(n1), find(n2)
        if r1 != r2:
            union(n1, n2)
        else:
            C.add(n1); C.add(n2)

    for n in range(1, N + 1):
        find(n)

    G = {P[cn] for cn in C}
    rlen = len({P[n] for n in range(1, N + 1) if P[n] not in G})
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
