import sys
from collections import deque

input = sys.stdin.readline

def solution(n, m, k, x, edges):
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in edges:
        graph[v1].append(v2)

    check = [-1] * (n + 1)
    check[x] = 0
    queue = deque([x])
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if check[next_node] == -1:
                check[next_node] = check[node] + 1
                queue.append(next_node)

    answer = list(filter(lambda entries: entries[1] == k, enumerate(check)))
    if not answer:
        print(-1)
    else:
        for idx, _ in sorted(answer):
            print(idx)

n, m, k, x = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
solution(n, m, k, x, edges)
