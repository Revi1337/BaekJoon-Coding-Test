import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def solution(n, r):
    graph = [[] for _ in range(n + 1)]
    for vertext1, vertext2 in edges:
        graph[vertext1].append(vertext2)
        graph[vertext2].append(vertext1)

    for vertext in range(1, n + 1):
        graph[vertext].sort(reverse=True)

    def dfs(vertext):
        nonlocal counter
        check[vertext] = counter
        counter += 1
        for next_vertext in graph[vertext]:
            if not check[next_vertext]:
                dfs(next_vertext)

    counter = 1
    check = [0] * (n + 1)
    dfs(r)

    for vertext in range(1, n + 1):
        print(check[vertext])


n, m, r = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
solution(n, r)