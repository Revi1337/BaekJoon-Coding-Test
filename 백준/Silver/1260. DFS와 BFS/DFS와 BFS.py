def solution(n, m, k, edges):
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    for idx, vertexts in enumerate(graph):
        vertexts.sort()

    check = [0] * (n + 1)
    def DFS(vertext):
        print(vertext, end = ' ')
        check[vertext] = 1
        for next_vertext in graph[vertext]:
            if check[next_vertext] == 0:
                DFS(next_vertext)

    def BFS(vertext):
        from collections import deque
        check = [0] * (n + 1)
        queue = deque()
        queue.append(vertext)
        check[vertext] = 1
        while queue:
            vertext_cnt = len(queue)
            for _ in range(vertext_cnt):
                vertext = queue.popleft()
                print(vertext, end = ' ')
                for next_vertext in graph[vertext]:
                    if check[next_vertext] == 0:
                        queue.append(next_vertext)
                        check[next_vertext] = 1
    
    DFS(k)
    print()
    BFS(k)
    print()

n, m, k = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
solution(n, m, k, edges)