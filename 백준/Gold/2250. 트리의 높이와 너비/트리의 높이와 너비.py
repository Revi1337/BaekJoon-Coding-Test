# 2026-04-26
# https://www.acmicpc.net/problem/2250
# 트리의 높이와 너비
# tree

import sys

input = sys.stdin.readline
sys.setrecursionlimit((10 ** 4) * 2)

def solution(V, E):

    def find_root():
        freq = [0] * (N + 1)
        for n, c1, c2 in E:
            freq[n] += 1
            if c1 != -1:
                freq[c1] += 1
            if c2 != -1:
                freq[c2] += 1
        return freq.index(min(freq[1:]))

    def inorder(n, depth):
        nonlocal col
        if tree[n][0] != -1:
            inorder(tree[n][0], depth + 1)

        lvs[depth] = lvs.setdefault(depth, [col, col])
        lvs[depth][0] = min(lvs[depth][0], col)
        lvs[depth][1] = max(lvs[depth][1], col)
        col += 1

        if tree[n][1] != -1:
            inorder(tree[n][1], depth + 1)

    tree = [[-1, -1] for _ in range(N + 1)]
    for n, c1, c2 in E:
        tree[n][0] = c1
        tree[n][1] = c2

    root = find_root()
    col, lvs = 1, {}
    inorder(root, 1)

    mx = max(lvs[key][1] - lvs[key][0] + 1 for key in lvs)
    for key in sorted(lvs.keys()):
        if lvs[key][1] - lvs[key][0] + 1 == mx:
            print(key, mx)
            return

N = int(input())
E = [list(map(int, input().split())) for _ in range(N)]
solution(N, E)