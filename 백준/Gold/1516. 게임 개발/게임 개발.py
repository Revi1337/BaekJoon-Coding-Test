from collections import deque

def solution(N, edges):
    priority = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    time = [0] * (N + 1)
    answer = [0] * (N + 1)
    for curr, edge in enumerate(edges, start = 1):
        time[curr] = edge[0]
        for need in edge[1:]:
            if need == -1:
                break
            priority[curr] += 1
            graph[need].append(curr)

    queue = deque()
    for curr in range(1, N + 1):
        if priority[curr] == 0:
            queue.append(curr)
            answer[curr] = time[curr]

    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            priority[next] -= 1
            answer[next] = max(answer[next], answer[curr] + time[next])
            if priority[next] == 0:
                queue.append(next)

    for ans in answer[1:]:
        print(ans)

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N)]
solution(N, edges)