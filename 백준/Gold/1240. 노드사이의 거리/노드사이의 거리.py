from collections import deque

"""BFS"""
def solution(N, M, E1, E2):

    def bfs(n1, n2):
        check = [-1] * (N + 1)
        check[n1] = 0
        queue = deque([n1])
        while queue:
            n = queue.popleft()
            if n == n2:
                return check[n2]
            for nn, nc in tree[n]:
                if check[nn] == -1:
                    check[nn] = check[n] + nc
                    queue.append(nn)

    tree = [[] for _ in range(N + 1)]
    for v1, v2, c in E1:
        tree[v1].append([v2, c])
        tree[v2].append([v1, c])

    ans = []
    for v1, v2 in E2:
        ans.append(bfs(v1, v2))

    print(*ans, sep = '\n')


N, M = map(int, input().split())
E1 = [list(map(int, input().split())) for _ in range(N - 1)]
E2 = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, E1, E2)
