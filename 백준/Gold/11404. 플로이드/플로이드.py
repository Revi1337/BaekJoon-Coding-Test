import sys

input = sys.stdin.readline

def solution(n, m, buses):
    vertext_cnt = n
    graph = [[1e9] * (vertext_cnt + 1) for _ in range(vertext_cnt + 1)]

    for bus in range(1, vertext_cnt + 1):
        graph[bus][bus] = 0

    for bus1, bus2, cost in buses:
        if graph[bus1][bus2] > cost:
            graph[bus1][bus2] = cost

    for bridge in range(1, vertext_cnt + 1):
        for bus1 in range(1, vertext_cnt + 1):
            for bus2 in range(1, vertext_cnt + 1):
                if graph[bus1][bridge] + graph[bridge][bus2] < graph[bus1][bus2]:
                    graph[bus1][bus2] = graph[bus1][bridge] + graph[bridge][bus2]

    for bus1 in range(1, vertext_cnt + 1):
        for bus2 in range(1, vertext_cnt + 1):
            if graph[bus1][bus2] == 1e9:
                print(0, end = ' ')
            else:
                print(graph[bus1][bus2], end = ' ')
        print()

n = int(input())
m = int(input())
buses = [list(map(int, input().split())) for _ in range(m)]
solution(n, m, buses)
