from collections import deque

def solution(A, B, N, M):
    dist = [-1] * 100_001
    dist[N] = 0
    queue = deque([N])

    while queue:
        n = queue.popleft()
        if n == M:
            return dist[M]
        for nn in [n - 1, n + 1, n - A, n + A, n - B, n + B, n * A, n * B]:
            if 0 <= nn <= 100_000 and dist[nn] == -1:
                dist[nn] = dist[n] + 1
                queue.append(nn)

A, B, N, M = map(int, input().split())
print(solution(A, B, N, M))