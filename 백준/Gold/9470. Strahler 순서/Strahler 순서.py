import sys
from collections import deque

input = sys.stdin.readline

def solution(K, M, P, E):
    counter, graph = [0] * (M + 1), [[] for _ in range(M + 1)]
    parent = [[] for _ in range(M + 1)]
    pri = [0] * (M + 1)
    queue = deque()
    for v1, v2 in E:
        counter[v2] += 1
        graph[v1].append(v2)
        parent[v2].append(v1)

    for n, cnt in enumerate(counter[1:], start=1):
        if not cnt:
            queue.append(n)
            pri[n] = 1

    while queue:
        n = queue.popleft()
        for nn in graph[n]:
            counter[nn] -= 1
            if not counter[nn]:
                seq = [pri[p] for p in parent[nn]]
                mx = max(seq) if seq else 0
                tmp = seq.count(mx)
                if tmp < 2:
                    pri[nn] = mx
                else:
                    pri[nn] = mx + 1
                queue.append(nn)

    return f'{K} {pri[M]}'

T = int(input())
for _ in range(T):
    K, M, P = map(int, input().split())
    E = [list(map(int, input().split())) for _ in range(P)]
    print(solution(K, M, P, E))