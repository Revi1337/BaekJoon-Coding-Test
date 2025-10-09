from collections import deque

"""
With BFS
"""
def solution(N, E):
    tree = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        tree[v1].append(v2)
        tree[v2].append(v1)

    parents = [0] * (N + 1)
    parents[1] = -1
    queue = deque([1])
    while queue:
        n = queue.popleft()
        for nn in tree[n]:
            if not parents[nn]:
                parents[nn] = n
                queue.append(nn)

    print(*parents[2:], end = '\n')

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
solution(N, E)