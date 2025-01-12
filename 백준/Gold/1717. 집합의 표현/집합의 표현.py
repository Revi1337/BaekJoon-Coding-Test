import sys

sys.setrecursionlimit(10 ** 5)

"""
V3. Advanced Union-Find (Include Path Compress & Rank)
"""
def solution(N, M, opers):

    def find(n):
        if tree[n] == n:
            return tree[n]

        tree[n] = find(tree[n])
        return tree[n]

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if rank[r1] < rank[r2]:
            tree[r1] = r2
        elif rank[r1] > rank[r2]:
            tree[r2] = r1
        else:
            tree[r2] = r1
            rank[r1] += 1

    rank = [0] * (N + 1)
    tree = [num for num in range(N + 1)]
    for oper, n1, n2 in opers:
        if not oper:
            union(n1, n2)
        else:
            r1, r2 = find(n1), find(n2)
            print('YES' if r1 == r2 else 'NO')

N, M = map(int, input().split())
opers = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, opers)
