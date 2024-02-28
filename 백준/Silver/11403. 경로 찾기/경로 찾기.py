def solution(vertext_cnt, graph):
    for bridge in range(vertext_cnt):
        for start in range(vertext_cnt):
            for end in range(vertext_cnt):
                if graph[start][bridge] and graph[bridge][end]:
                    graph[start][end] = 1

    for row in range(vertext_cnt):
        for col in range(vertext_cnt):
            print(graph[row][col], end = ' ')
        print()

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
solution(n, graph)