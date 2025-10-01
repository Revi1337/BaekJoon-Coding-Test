# 2025-10-01
# https://www.acmicpc.net/problem/1062

import sys
import string

input = sys.stdin.readline

def solution(N, K, W):
    if K < 5:
        return 0
    if K == 26:
        return N

    def backtrack(lst, st, limit):
        if len(lst) == limit:
            combs.append([*lst])
            return
        for idx in range(st, len(cache)):
            lst.append(cache[idx])
            backtrack(lst, idx + 1, limit)
            lst.pop()

    fix = {'a', 'n', 't', 'i', 'c'}
    cache = [char for char in set(list(string.ascii_lowercase)) - fix]
    W = [set(w[4:-4]) - fix for w in W]
    combs = []
    backtrack([], 0, K - 5)

    mx = 0
    for comb in combs:
        cnt = 0
        known = fix.union(comb)
        for w in W:
            if w.issubset(known):
                cnt += 1
        mx = max(mx, cnt)

    return mx

N, K = map(int, input().split())
W = [input().rstrip() for _ in range(N)]
print(solution(N, K, W))