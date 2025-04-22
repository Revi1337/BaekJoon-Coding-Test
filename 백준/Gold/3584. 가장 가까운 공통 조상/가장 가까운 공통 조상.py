import sys

sys.setrecursionlimit(10 ** 6)

def solution(N, edges, A, B):

    def dfs(n):
        for nxt in graph[n]:
            if not check[nxt]:
                check[nxt] = 1
                t.append(nxt)
                dfs(nxt)

    graph = [[] for _ in range(N + 1)]
    for v1, v2 in edges:
        graph[v2].append(v1)

    answer = []

    check = [0] * (N + 1)
    check[A] = 1
    t = [A]
    dfs(A)
    answer.append(t)

    check = [0] * (N + 1)
    check[B] = 1
    t = [B]
    dfs(B)
    answer.append(t)

    for node in answer[0]:
        if check[node]:
            return node

T = int(input())
for _ in range(T):
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    A, B = map(int, input().split())
    print(solution(N, edges, A, B))