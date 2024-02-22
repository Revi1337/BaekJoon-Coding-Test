def solution(n, computers):
    vertext_cnt = n
    graph = [[] for _ in range(vertext_cnt)]
    for computer, vertexts in enumerate(computers):
        for vertext, value in enumerate(vertexts):
            if value: graph[computer].append(vertext)

    check = [0] * vertext_cnt
    def dfs(vertext):
        check[vertext] = 1
        for next_vertext in graph[vertext]:
            if not check[next_vertext]:
                dfs(next_vertext)

    answer = 0
    for vertext in range(vertext_cnt):
        if graph[vertext] and not check[vertext]:
            answer += 1
            dfs(vertext)

    return answer