from collections import deque

def solution(N, K):
    MAX = 200_001
    dist = [-1] * MAX
    count = [0] * MAX

    queue = deque([N])
    dist[N], count[N] = 0, 1

    while queue:
        curr = queue.popleft()
        for next in (curr - 1, curr + 1, curr * 2):
            if 0 <= next < MAX:
                if dist[next] == -1:
                    dist[next] = dist[curr] + 1
                    count[next] = count[curr]
                    queue.append(next)
                elif dist[next] == dist[curr] + 1:
                    count[next] += count[curr]

    print(dist[K])
    print(count[K])

N, K = map(int, input().split())
solution(N, K)