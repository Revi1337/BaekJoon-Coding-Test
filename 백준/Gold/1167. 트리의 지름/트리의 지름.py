from collections import deque

def solution(vertext_cnt, edges):
    graph = [[] for _ in range(vertext_cnt + 1)]
    for v, nv, nc in edges:
        graph[v].append([nv, nc])
        graph[nv].append([v, nc])

    distance = [-1] * (vertext_cnt + 1)
    def dfs(vertext):
        for next_vertext, next_cost in graph[vertext]:
            if distance[next_vertext] == -1:
                distance[next_vertext] = distance[vertext] + next_cost
                dfs(next_vertext)

    def bfs(vertext):
        distance = [-1] * (vertext_cnt + 1)
        distance[vertext] = 0
        queue = deque([vertext])
        while queue:
            curr_vertext = queue.popleft()
            for next_vertext, next_cost in graph[curr_vertext]:
                if distance[next_vertext] == -1:
                    distance[next_vertext] = distance[curr_vertext] + next_cost
                    queue.append(next_vertext)
        return max(distance)

    distance[1] = 0
    dfs(1)
    far_vertext = distance.index(max(distance))

    answer = bfs(far_vertext)

    return answer

v = int(input())
edges = []
for _ in range(v):
    datas = list(map(int, input().split()))
    vertext, metadatas = datas[0], datas[1:-1]
    for idx in range(0, len(metadatas), 2):
        next_vertext, next_cost = metadatas[idx], metadatas[idx + 1]
        edges.append([vertext, next_vertext, next_cost])

print(solution(v, edges))


