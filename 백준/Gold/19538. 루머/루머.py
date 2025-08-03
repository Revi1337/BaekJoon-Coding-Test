import sys

input = sys.stdin.readline

from collections import deque

def solution(N, G, M, S):
    queue, time = deque(), [-1] * (N + 1)
    G.insert(0, [])
    for lst in G[1:]:
        lst.pop()

    for s in S:
        time[s] = 0
        queue.append(s)

    t = 1
    while queue:
        lst = []
        for _ in range(len(queue)):
            n = queue.popleft()
            for nn in G[n]:
                if time[nn] == -1:
                    lst.append(nn)

        nxt = []
        for n in lst:
            cnt = 0
            for nn in G[n]:
                if time[nn] != -1:
                    cnt += 1
            if cnt >= len(G[n]) // 2 + int(bool(len(G[n]) % 2)):
                nxt.append(n)

        for n in nxt:
            time[n] = t
            queue.append(n)
        t += 1

    return time[1:]

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
S = list(map(int, input().split()))
print(*solution(N, G, M, S), sep = ' ')