import sys
from collections import deque

input = sys.stdin.readline

def solution(N, M, E):
    INF, ST, END = -float('inf'), 1, N
    costs, trace = [INF] * (N + 1), [0] * (N + 1)

    costs[ST], trace[ST], neg = 0, ST, set()
    for seq in range(N):
        for v1, v2, c in E:
            if costs[v2] < costs[v1] + c:
                trace[v2], costs[v2] = v1, costs[v1] + c
                if seq == N - 1:
                    neg.add(v2)

    if costs[N] == -INF:
        print(-1)
        return

    graph = [[] for _ in range(N + 1)]
    for v1, v2, c in E:
        graph[v1].append(v2)
    for n in neg:
        check = [0] * (N + 1)
        check[n] = 1
        queue = deque([n])
        while queue:
            n = queue.popleft()
            if n == END:
                print(-1)
                return
            for nn in graph[n]:
                if not check[nn]:
                    check[nn] = 1
                    queue.append(nn)

    st, ans = END, []
    while st != trace[st]:
        ans.append(st)
        st = trace[st]
    ans.append(ST)
    print(*ans[::-1])


N, M = map(int, input().split())
E = [list(map(int, input().rstrip().split())) for _ in range(M)]
solution(N, M, E)