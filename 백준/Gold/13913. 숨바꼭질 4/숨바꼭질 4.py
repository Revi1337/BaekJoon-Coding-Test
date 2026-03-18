# 2026-03-18
# https://www.acmicpc.net/problem/13913
# bfs

from collections import deque

def solution(N, K):
    check, trace = [[-1] * 200_001 for _ in range(2)]
    check[N] = 0
    queue = deque([N])

    while queue:
        curr = queue.popleft()
        if curr == K:
            print(check[curr])
            foot = [K]
            while trace[K] != -1:
                foot.append(trace[K])
                trace[K] = trace[trace[K]]
            print(*foot[::-1])
            return
        for nxt in curr - 1, curr + 1, curr * 2:
            if 0 <= nxt <= 200_000 and check[nxt] == -1:
                check[nxt] = check[curr] + 1
                trace[nxt] = curr
                queue.append(nxt)

N, K = map(int, input().split())
solution(N, K)
