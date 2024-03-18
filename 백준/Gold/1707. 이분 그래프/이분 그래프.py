from collections import deque
import sys

input = sys.stdin.readline

def solution(v, e, edges):
    graph = [[] for _ in range(v + 1)]
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    check = [0] * (v + 1)
    result = True
    for vertext in range(1, v + 1):
        if not check[vertext]:
            check[vertext] = 1
            queue = deque([vertext])
            while queue:
                node = queue.popleft()
                for next_node in graph[node]:
                    if not check[next_node]:
                        if check[node] == 1:
                            check[next_node] = 2
                        else:
                            check[next_node] = 1
                        queue.append(next_node)
                    else:
                        if check[node] == check[next_node]:
                            result = False
        if not result:
            break
    return 'YES' if result else 'NO'

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    print(solution(v, e, edges))
