def solution(n, computers):
    vertext_cnt = n
    graph = [[] for _ in range(vertext_cnt + 1)]
    for computer, vertexts in enumerate(computers, start=1):
        for vertext, value in enumerate(vertexts, start=1):
            if value: graph[computer].append(vertext)

    check = [0] * (vertext_cnt + 1)
    def dfs(vertext):
        check[vertext] = 1
        for next_vertext in graph[vertext]:
            if not check[next_vertext]:
                dfs(next_vertext)

    answer = 0
    for vertext in range(1, vertext_cnt + 1):
        if graph[vertext] and not check[vertext]:
            answer += 1
            dfs(vertext)

    return answer