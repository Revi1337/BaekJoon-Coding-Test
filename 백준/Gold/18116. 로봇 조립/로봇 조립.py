# 2026-04-19
# https://www.acmicpc.net/problem/18116
# 로봇 조립
# Union-Find

def solution(N, E):

    LIMIT = 1_000_001

    def find(n):
        while n != parents[n]:
            parents[n] = parents[parents[n]]
            n = parents[n]
        return n

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if r1 < r2:
            parents[r2] = r1
            cnts[r1] += cnts[r2]
        else:
            parents[r1] = r2
            cnts[r2] += cnts[r1]

    parents, cnts = list(range(LIMIT)), [1] * LIMIT
    for lst in E:
        if lst[0] == 'I':
            n1, n2 = map(int, lst[1:])
            if find(n1) != find(n2):
                union(n1, n2)
        else:
            n = int(lst[1])
            print(cnts[find(n)])

N = int(input())
E = [input().rstrip().split() for _ in range(N)]
solution(N, E)
