# 2026-04-27
# https://www.acmicpc.net/problem/17472
# 다리 만들기 2
# MST
# kruskal
# 간선을 어떻게 만들것인가가 관건인 문제 ㅇㅇ

import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    def find(n):
        while n != parents[n]:
            parents[n] = parents[parents[n]]
            n = parents[n]
        return n

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if r1 == r2:
            return False
        if r1 < r2:
            parents[r2] = r1
        else:
            parents[r1] = r2
        return True

    label, nodes, check = 1, [], [[0] * M for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if arr[row][col] and not check[row][col]:
                check[row][col] = 1
                stack = [[row, col]]
                nn = []
                while stack:
                    r, c = stack.pop()
                    nn.append([r, c])
                    arr[r][c] = label
                    for d in range(4):
                        nrow, ncol = r + drow[d], c + dcol[d]
                        if inside(nrow, ncol) and not check[nrow][ncol] and arr[nrow][ncol]:
                            check[nrow][ncol] = 1
                            stack.append([nrow, ncol])
                nodes.append(nn)
                label += 1

    E = []
    for lst in nodes:
        lab = arr[lst[0][0]][lst[0][1]]
        for row, col in lst:
            for d in range(4):
                dist = 0
                nrow, ncol = row + drow[d], col + dcol[d]
                while inside(nrow, ncol) and not arr[nrow][ncol]:
                    dist += 1
                    nrow, ncol = nrow + drow[d], ncol + dcol[d]
                if inside(nrow, ncol) and arr[nrow][ncol]:
                    olab = arr[nrow][ncol]
                    if lab != olab and dist > 1:
                        E.append([lab, olab, dist])

    parents = list(range(label))
    E.sort(key=lambda x: x[2])
    ans = 0
    for n1, n2, c in E:
        if union(n1, n2):
            ans += c

    tmp_root = find(1)
    for n in range(1, label):
        if find(n) != tmp_root:
            return -1

    return ans

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, arr))