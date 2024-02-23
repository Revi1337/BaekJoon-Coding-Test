def solution(n, m, edges):
    vertext_cnt = n
    graph = [[] for _ in range(vertext_cnt + 1)]
    for vertext1, vertext2 in edges:
        graph[vertext1].append(vertext2)
        graph[vertext2].append(vertext1)

    def dfs(vertext):
        check[vertext] = 1
        for next_vertext in graph[vertext]:
            if not check[next_vertext]:
                dfs(next_vertext)

    check = [0] * (vertext_cnt + 1)
    answer = 0
    for vertext in range(1, vertext_cnt + 1):
        if not check[vertext]:
            answer += 1
            dfs(vertext)

    return answer

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, edges))