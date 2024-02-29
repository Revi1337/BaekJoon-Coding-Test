from collections import deque
import sys

sys.setrecursionlimit(10 ** 5)

def solution(vertext_cnt, edges):
    graph = [[] for _ in range(vertext_cnt + 1)]
    for vertext1, vertext2, cost in edges:
        graph[vertext1].append([vertext2, cost])
        graph[vertext2].append([vertext1, cost])

    distance = [-1] * (vertext_cnt + 1)
    def dfs(vertext):
        for next_vertext, next_cost in graph[vertext]:
            if distance[next_vertext] == -1:
                distance[next_vertext] = distance[vertext] + next_cost
                dfs(next_vertext)

    def bfs(vertext):
        distance = [-1] * (vertext_cnt + 1)
        queue = deque([vertext])
        distance[vertext] = 0
        while queue:
            vertext = queue.popleft()
            for next_vertext, next_cost in graph[vertext]:
                if distance[next_vertext] == -1:
                    distance[next_vertext] = distance[vertext] + next_cost
                    queue.append(next_vertext)
        return distance

    distance[1] = 0
    dfs(1)

    far_vertext = distance.index(max(distance))
    distance = bfs(far_vertext)

    return max(distance)

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
print(solution(n, edges))
