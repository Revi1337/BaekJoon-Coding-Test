# 2025-09-29
# https://www.acmicpc.net/problem/1043

import sys

input = sys.stdin.readline

def solution(N, M, arr, P):

    def find(n):
        if n == parents[n]:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if r1 < r2:
            parents[r2] = r1
        else:
            parents[r1] = r2

    parents = list(range(N + 1))
    for p in P:
        p = p[1:]
        for idx in range(len(p) - 1):
            union(p[idx], p[idx + 1])

    ans = 0
    arr = set(find(h) for h in arr[1:])
    for p in P:
        for h in p[1:]:
            if find(h) in arr:
                break
        else:
            ans += 1

    return ans

N, M = map(int, input().split())
arr = list(map(int, input().split()))
P = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, arr, P))
