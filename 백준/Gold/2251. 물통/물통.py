import sys
from collections import deque

input = sys.stdin.readline

def solution(A, B, C):
    check = [[0] * 401 for _ in range(401)]
    check[200][200 - C] = 1
    queue = deque([[0, 0, C]])
    ans = set()

    while queue:
        a, b, c = queue.popleft()
        if a == 0:
            ans.add(c)

        am = min(a, B - b)
        na, nb, nc = a - am, b + am, c
        if not check[na][nb]:
            check[na][nb] = 1
            queue.append([na, nb, nc])
        am = min(a, C - c)
        na, nb, nc = a - am, b, c + am
        if not check[na][nb]:
            check[na][nb] = 1
            queue.append([na, nb, nc])

        am = min(b, A - a)
        na, nb, nc = a + am, b - am, c
        if not check[na][nb]:
            check[na][nb] = 1
            queue.append([na, nb, nc])
        am = min(b, C - c)
        na, nb, nc = a, b - am, c + am
        if not check[na][nb]:
            check[na][nb] = 1
            queue.append([na, nb, nc])

        am = min(c, A - a)
        na, nb, nc = a + am, b, c - am
        if not check[na][nb]:
            check[na][nb] = 1
            queue.append([na, nb, nc])
        am = min(c, B - b)
        na, nb, nc = a, b + am, c - am
        if not check[na][nb]:
            check[na][nb] = 1
            queue.append([na, nb, nc])

    return sorted(ans)

A, B, C = map(int, input().split())
print(*solution(A, B, C))