# 2026-04-25
# https://www.acmicpc.net/problem/15681
# 트리와 쿼리
# tree
# dfs(post order + tree dp)
# 아 시이이발 설마.  input = sys.stdin.readline 문제냐? 

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

def solution(N, R, Q, E, U):

    def make_tree(n, pn):
        cnt = 1
        for nn in tree[n]:
            if nn != pn:
                cnt += make_tree(nn, n)

        memo[n] += cnt
        return memo[n]

    tree = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        tree[v1].append(v2)
        tree[v2].append(v1)

    memo = [0] * (N + 1)
    make_tree(R, -1)

    print(*[memo[u] for u in U], sep = '\n')

N, R, Q = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(N - 1)]
U = [int(input()) for _ in range(Q)]
solution(N, R, Q, E, U)