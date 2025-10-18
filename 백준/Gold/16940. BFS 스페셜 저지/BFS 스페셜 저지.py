import sys
from collections import deque

input = sys.stdin.readline

def solution(N, E, seq):
    graph = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        graph[v1].append(v2)
        graph[v2].append(v1)

    childs = [[] for _ in range(N + 1)]
    check = [0] * (N + 1)
    check[1] = 1
    queue = deque([1])
    while queue:
        n = queue.popleft()
        for nn in graph[n]:
            if not check[nn]:
                childs[n].append(nn)
                check[nn] = check[n] + 1
                queue.append(nn)

    queue = deque([1])
    st = 1
    while queue:
        n = queue.popleft()
        a = set(childs[n])
        length = len(a)
        b = seq[st:st + length]
        queue.extend(b)
        b = set(b)
        st += length

        if a != b:
            return 0
    return 1

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
seq = list(map(int, input().split()))
print(solution(N, E, seq))
