from collections import deque

def solution(N, M, bridges, start, end):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in bridges:
        graph[a].append((b, c))
        graph[b].append((a, c))

    def bfs(weight):
        visited = [False] * (N + 1)
        queue = deque([start])
        visited[start] = True
        while queue:
            cur = queue.popleft()
            for nxt, limit in graph[cur]:
                if not visited[nxt] and limit >= weight:
                    visited[nxt] = True
                    queue.append(nxt)
        return visited[end]

    left, right = 1, 1_000_000_000
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if bfs(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

N, M = map(int, input().split())
bridges = [list(map(int, input().split())) for _ in range(M)]
start, end = map(int, input().split())
print(solution(N, M, bridges, start, end))