# 2026-04-25
# https://www.acmicpc.net/problem/1068
# 트리
# tree
# dfs(post order 개념을 이용)

def solution(N, P, R):

    def cnt_leafs(n):
        if n == R:
            return 0
        childs = [c for c in tree[n] if c != R]
        if not childs:
            return 1
        cnt = 0
        for c in childs:
            cnt += cnt_leafs(c)
        return cnt

    root, tree = None, [[] for _ in range(N)]
    for n, pn in enumerate(P):
        if pn == -1:
            root = n
        else:
            tree[pn].append(n)

    return cnt_leafs(root)

N = int(input())
P = list(map(int, input().split()))
R = int(input())
print(solution(N, P, R))