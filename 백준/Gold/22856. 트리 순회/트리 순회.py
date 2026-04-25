# 2026-04-25
# https://www.acmicpc.net/problem/22856
# 트리 순회
# tree
# dfs

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

"""
이동 횟수 = 2 * (N - 1) - (루트 -> 마지막 노드 거리)
"""
def solution(N, E):

    def find_last():
        last = 1
        while tree[last][1] != -1:
            last = tree[last][1]
        return last

    def root_to_last(n, depth):
        if n == last:
            return depth
        for nn in tree[n]:
            if nn != -1:
                d = root_to_last(nn, depth + 1)
                if d != -1:
                    return d
        return -1

    tree = [[-1, -1] for _ in range(N + 1)]
    for pn, left, right in E:
        tree[pn][0] = left
        tree[pn][1] = right

    root = 1
    last = find_last()
    dist = root_to_last(root, 0)

    return 2 * (N - 1) - dist

N = int(input())
E = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, E))