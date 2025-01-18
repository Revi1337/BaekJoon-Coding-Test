def solution(seq, N, K, edges, M, relations):

    def find(n):
        if tree[n] == n:
            return n

        tree[n] = find(tree[n])
        return tree[n]

    def union(n1, n2):
        root1, root2 = find(n1), find(n2)
        if root2 > root1:
            tree[root2] = root1
        else:
            tree[root1] = root2

    tree = list(range(N))
    for v1, v2 in edges:
        union(v1, v2)

    print(f'Scenario {seq + 1}:')
    for t1, t2 in relations:
        print(1 if find(t1) == find(t2) else 0)

T = int(input())
for idx in range(T):
    N = int(input())
    K = int(input())
    edges = [list(map(int, input().split())) for _ in range(K)]
    M = int(input())
    relations = [list(map(int, input().split())) for _ in range(M)]
    solution(idx, N, K, edges, M, relations)
    print()