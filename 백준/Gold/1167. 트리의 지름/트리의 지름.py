import sys
from collections import deque

input = sys.stdin.readline

def solution(V, E):
    graph = [[] for _ in range(V + 1)]
    for lst in E:
        for idx in range(1, len(lst) - 1, 2):
            graph[lst[0]].append([lst[idx], lst[idx + 1]])

    queue = deque([1])
    check = [-1] * (V + 1)
    far = check[1] = 1
    while queue:
        n = queue.popleft()
        if check[n] > check[far]:
            far = n
        for nn, nc in graph[n]:
            if check[nn] == -1:
                check[nn] = check[n] + nc
                queue.append(nn)

    ans = 0
    queue = deque([far])
    check = [-1] * (V + 1)
    check[far] = 0
    while queue:
        n = queue.popleft()
        ans = max(ans, check[n])
        for nn, nc in graph[n]:
            if check[nn] == -1:
                check[nn] = check[n] + nc
                queue.append(nn)

    return ans

V = int(input())
E = [list(map(int, input().split())) for _ in range(V)]
print(solution(V, E))