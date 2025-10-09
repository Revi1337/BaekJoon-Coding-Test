from collections import deque

def solution(N, E):
    tree = [[] for _ in range(N + 1)]
    for v1, v2, c in E:
        tree[v1].append([v2, c])
        tree[v2].append([v1, c])

    mx, mxn = -1e9, None
    queue = deque([[1, -1, 0]])
    while queue:
        n, pn, c = queue.popleft()
        if c > mx:
            mx, mxn = c, n
        for nn, nc in tree[n]:
            if nn != pn:
                queue.append([nn, n, c + nc])

    ans = 0
    queue = deque([[mxn, -1, 0]])
    while queue:
        n, pn, c = queue.popleft()
        ans = max(c, ans)
        for nn, nc in tree[n]:
            if nn != pn:
                queue.append([nn, n, c + nc])

    return ans

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
print(solution(N, E))
