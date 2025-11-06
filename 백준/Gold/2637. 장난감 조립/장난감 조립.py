import sys
from collections import deque

input = sys.stdin.readline

def solution(N, M, E):
    dag, ind = [[] for _ in range(N + 1)], [0] * (N + 1)
    for x, y, k in E:
        dag[y].append([x, k])
        ind[x] += 1

    basic = [n for n in range(1, N + 1) if not ind[n]]
    ans = [[0] * (N + 1) for _ in range(N + 1)]
    queue = deque()
    for n in basic:
        ans[n][n] = 1
        queue.append(n)

    while queue:
        n = queue.popleft()
        for nn, k in dag[n]:
            for idx in range(1, N + 1):
                ans[nn][idx] += ans[n][idx] * k
            ind[nn] -= 1
            if ind[nn] == 0:
                queue.append(nn)

    for n in basic:
        print(n, ans[N][n])

N = int(input())
M = int(input())
E = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, E)