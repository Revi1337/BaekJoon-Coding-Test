import sys

sys.setrecursionlimit(10 ** 5)

def solution(n, edges):
    vertext_cnt = n
    graph = [[] for _ in range(vertext_cnt + 1)]
    check = [0] * (vertext_cnt + 1)

    for vertext1, vertext2 in edges:
        graph[vertext1].append(vertext2)
        graph[vertext2].append(vertext1)

    def dfs(vertext):
        check[vertext] = 1
        for next_vertext in graph[vertext]:
            if not check[next_vertext]:
                tracking[next_vertext] = vertext
                dfs(next_vertext)

    tracking = [0] * (vertext_cnt + 1)
    tracking[1] = 1
    dfs(1)
    for vertext in range(2, vertext_cnt + 1):
        print(tracking[vertext])

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
solution(n, edges)
