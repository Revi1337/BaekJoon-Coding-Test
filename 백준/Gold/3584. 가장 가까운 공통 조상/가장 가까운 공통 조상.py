# 2026-04-25
# https://www.acmicpc.net/problem/3584
# 가장 가까운 공통 조상 (LCA 최적화 전으로 푸는 문제 ㅇㅇ depth 직접 비교 방식)
# tree
# dfs

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

"""
1. root 를 구한다.
2. 간선들로 conn 생성
3. make_tree 에서 각 정점의 부모노드와 각 정점의 depth 를 구한다.
4. V1, V2 의 깊이를 맞춘다.
5. V1, V2 같이 같아질때까지 맞춘다.
6. 반환한다.
"""
def solution(N, E, V1, V2):

    def find_root():
        freq = [0] * (N + 1)
        for v1, v2 in E:
            freq[v2] += 1
        for n, cnt in enumerate(freq[1:], start=1):
            if not cnt:
                return n
        return None # Impossible

    def make_tree(n, pn):
        for nn in conn[n]:
            if nn != pn:
                parents[nn] = n
                depths[nn] = depths[n] + 1
                make_tree(nn, n)

    conn = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        conn[v1].append(v2)

    depths, parents = [[0] * (N + 1) for _ in range(2)]
    make_tree(find_root(), -1)

    mxn, mnn = (V2, V1) if depths[V1] < depths[V2] else (V1, V2)
    dd = depths[mxn] - depths[mnn] # aka. diff of depth
    while dd > 0:
        mxn = parents[mxn]
        dd -= 1

    while mxn != mnn:
        mxn, mnn = parents[mxn], parents[mnn]
        
    return mxn

T = int(input())
for _ in range(T):
    N = int(input())
    E = [list(map(int, input().split())) for _ in range(N - 1)]
    V1, V2 = map(int, input().split())
    print(solution(N, E, V1, V2))

