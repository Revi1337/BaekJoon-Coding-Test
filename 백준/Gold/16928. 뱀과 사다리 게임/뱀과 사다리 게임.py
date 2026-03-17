# 2026-03-15
# https://www.acmicpc.net/problem/16928
# bfs

from collections import deque

def solution(N, M, arr1, arr2):
    carr1, carr2 = [[0] * 101 for _ in range(2)]
    for fro, to in arr1:
        carr1[fro] = to
    for fro, to in arr2:
        carr2[fro] = to

    check = [0] * 101
    check[1] = 1
    queue = deque([1])
    while queue:
        curr = queue.popleft()
        if curr == 100:
            return check[100] - 1
        for nxt in range(curr + 1, curr + 7):
            if 1 <= nxt <= 100:
                if carr1[nxt]:
                    nxt = carr1[nxt]
                elif carr2[nxt]:
                    nxt = carr2[nxt]

                if not check[nxt]:
                    check[nxt] = check[curr] + 1
                    queue.append(nxt)

N, M = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, arr1, arr2))