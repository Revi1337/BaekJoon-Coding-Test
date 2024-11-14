from collections import deque

def solution(size, entry, edges):
    max_vertext = max(edges)
    graph = [[] for _ in range(max_vertext + 1)]
    for idx in range(0, len(edges), 2):
        graph[edges[idx]].append(edges[idx + 1])

    distance = [0] * (max_vertext + 1)
    distance[entry] = 1
    queue = deque([entry])
    while queue:
        vertext = queue.popleft()
        for next_vertext in graph[vertext]:
            if not distance[next_vertext]:
                distance[next_vertext] = distance[vertext] + 1
                queue.append(next_vertext)

    max_distance = max(distance)
    answer = None
    for vertext in range(max_vertext + 1):
        if distance[vertext] == max_distance:
            answer = vertext

    return answer


T = 10
for index in range(T):
    size, entry = map(int, input().split())
    edges = list(map(int, input().split()))
    print(f'#{index + 1} {solution(size, entry, edges)}')
