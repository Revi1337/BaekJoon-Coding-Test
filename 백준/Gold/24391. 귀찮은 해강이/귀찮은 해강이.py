# 2026-04-19
# https://www.acmicpc.net/problem/24391
# 귀찮은 해강이

def solution(N, M, E, arr):

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

    parents = list(range(N + 1))
    for n1, n2 in E:
        union(n1, n2)

    ans, curr = 0, find(arr[0])
    for n in arr:
        p = find(n)
        if p != curr:
            ans += 1
            curr = p

    return ans

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
arr = list(map(int, input().split()))
print(solution(N, M, E, arr))
