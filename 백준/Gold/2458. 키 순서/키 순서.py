import sys

input = sys.stdin.readline

def solution(n, m, edges):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for v1, v2 in edges:
        graph[v1][v2] = 1

    for bridge in range(1, n + 1):
        for from_ in range(1, n + 1):
            for to_ in range(1, n + 1):
                if graph[from_][bridge] == 1 and graph[bridge][to_] == 1:
                    graph[from_][to_] = 1

    answer = [0] * (n + 1)
    for from_ in range(1, n + 1):
        for to_ in range(1, n + 1):
            if graph[from_][to_] == 1:
                answer[from_] += 1
                answer[to_] += 1

    return answer.count(n - 1)

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, edges))