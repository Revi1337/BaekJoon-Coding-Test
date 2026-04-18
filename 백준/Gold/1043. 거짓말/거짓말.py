# 2026-04-18
# https://www.acmicpc.net/problem/1043
# 거짓말
# DataStructure(Set) or Union-Find

def solution(N, M, T, E):
    truth = set(T[1:])
    for _ in range(M):
        for lst in E:
            parti = set(lst[1:])
            if truth & parti:
                truth = truth.union(parti)

    ans = 0
    for lst in E:
        parti = set(lst[1:])
        if not truth & parti:
            ans += 1

    return ans

N, M = map(int, input().split())
T = list(map(int, input().split()))
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, T, E))