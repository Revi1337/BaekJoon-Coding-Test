import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def solution(N, E):

    WOLF, SHEEP = 'W', 'S'

    def dfs(n, pn):
        sm = 0
        for nn in tree[n]:
            if nn != pn:
                sm += dfs(nn, n)

        if sign[n] == WOLF:
            amount[n] = max(0, sm - amount[n])
        else:
            amount[n] += sm

        return amount[n]

    tree = [[] for _ in range(N + 1)]
    sign, amount = [''] * (N + 1), [0] * (N + 1)

    for n, (t, a, p) in enumerate(E, start=2):
        a, n, p = int(a), int(n), int(p)
        sign[n], amount[n] = t, a
        tree[n].append(p)
        tree[p].append(n)

    dfs(1, -1)
    return amount[1]

N = int(input())
E = [input().rstrip().split() for _ in range(N - 1)]
print(solution(N, E))