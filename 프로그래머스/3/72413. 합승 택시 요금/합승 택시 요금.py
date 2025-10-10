
"""
다익스트라 or 플로이드 워셜
"""
def solution(n, s, a, b, fares):
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for n in range(1, n + 1):
        dist[n][n] = 0
    
    for v1, v2, cost in fares:
        dist[v1][v2] = cost
        dist[v2][v1] = cost
        
    for mid in range(1, n + 1):
        for st in range(1, n + 1):
            for end in range(1, n + 1):
                if dist[st][mid] + dist[mid][end] < dist[st][end]:  
                    dist[st][end] = dist[st][mid] + dist[mid][end]
                    
    ans = dist[a][s] + dist[b][s]
    for st in range(1, n + 1):
        ans = min(ans, dist[s][st] + dist[a][st] + dist[b][st])

    return ans