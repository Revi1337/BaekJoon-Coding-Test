from collections import deque

def solution(info, edges):
    length = len(info)
    graph = [[] for _ in range(length)]
    for vertext1, vertext2 in edges:
        graph[vertext1].append(vertext2)

    max_sheep = 0
    queue = deque([(0, 1, 0, set())])
    while queue:
        current, sheep_count, wolf_count, visited = queue.popleft()
        max_sheep = max(max_sheep, sheep_count)
        visited.update(graph[current])
        for next_node in visited:
            if info[next_node]:
                if sheep_count != wolf_count + 1:
                    queue.append((next_node, sheep_count, wolf_count + 1, visited - {next_node}))
            else:
                queue.append((next_node, sheep_count + 1, wolf_count, visited - {next_node}))
    return max_sheep