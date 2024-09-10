import sys

input = sys.stdin.readline

"""
촌수계산 (https://www.acmicpc.net/problem/2644)
2024-09-10
"""

def solution(N, T, length, edges):
    graph = [[] for _ in range(N + 1)]
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(v):
        for nv in graph[v]:
            if distance[nv] == -1:
                distance[nv] = distance[v] + 1
                dfs(nv)

    distance = [-1] * (N + 1)
    distance[T[0]] = 0
    dfs(T[0])

    return distance[T[1]]

N = int(input())
T = list(map(int, input().split()))
length = int(input())
edges = [list(map(int, input().split())) for _ in range(length)]
print(solution(N, T, length, edges))
