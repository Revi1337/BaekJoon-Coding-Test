# 2026-03-17
# https://www.acmicpc.net/problem/12851
# bfs

from collections import deque

def solution(N, K):
    cnts, check = [[0] * 200_001 for _ in range(2)]
    cnts[N] = check[N] = 1
    queue = deque([N])
    while queue:
        curr = queue.popleft()
        for nxt in curr - 1, curr + 1, curr * 2:
            if 0 <= nxt <= 200_000:
                if not check[nxt]:
                    check[nxt] = check[curr] + 1
                    cnts[nxt] = cnts[curr]
                    queue.append(nxt)
                elif check[nxt] == check[curr] + 1:
                    cnts[nxt] += cnts[curr]

    print(*[check[K] - 1, cnts[K]], sep = '\n')

N, K = map(int, input().split())
solution(N, K)