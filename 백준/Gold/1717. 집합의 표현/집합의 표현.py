import sys

sys.setrecursionlimit(10 ** 5)

"""
V3. Basic Union-Find (Include Rank & Path Compress)
"""
def solution(N, M, opers):

    def find(n):
        if tree[n] == n:
            return tree[n]

        tree[n] = find(tree[n])
        return tree[n]

    tree = [num for num in range(N + 1)]
    for oper, n1, n2 in opers:
        r1, r2 = find(n1), find(n2)
        if not oper:
            tree[r1] = r2
        else:
            print('YES' if r1 == r2 else 'NO')

N, M = map(int, input().split())
opers = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, opers)
