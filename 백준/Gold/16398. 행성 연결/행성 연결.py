import heapq

def solution(N, dist):
    conn, pq, ans = [0] * N, [[0, 0]], 0

    while pq:
        cost, n = heapq.heappop(pq)
        if conn[n]:
            continue
        conn[n] = 1
        ans += cost
        for nn, nc in enumerate(dist[n]):
            if dist[n][nn] != 0 and not conn[nn]:
                heapq.heappush(pq, (nc, nn))

    return ans

N = int(input())
dist = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, dist))