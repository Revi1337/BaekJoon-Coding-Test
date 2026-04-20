# 2026-04-20
# https://www.acmicpc.net/problem/1939
# 중량제한
# V3. Binary Search + Kruskal 변형 (간선 내림차순 + Union-Find 기반 연결 가능성 판별)

def solution(N, M, E, arr):

    st, end = arr

    def find(n):
        while n != parents[n]:
            parents[n] = parents[parents[n]]
            n = parents[n]
        return n

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if r1 < r2:
            parents[r2] = r1
        else:
            parents[r1] = r2

    def possible(lim):
        for a, b, c in E:
            if c >= lim:
                union(a, b)
                if find(st) == find(end):
                    return True
        return False

    E.sort(key=lambda x: -x[2])

    left, right = 1, 1_000_000_000
    while left <= right:
        mid = (left + right) // 2
        parents = list(range(N + 1))
        if possible(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
arr = list(map(int, input().split()))
print(solution(N, M, E, arr))