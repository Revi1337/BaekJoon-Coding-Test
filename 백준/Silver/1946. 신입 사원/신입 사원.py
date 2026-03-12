# 2026-03-11
# https://www.acmicpc.net/problem/2512
# greedy

def solution(N, arr):
    arr.sort()
    ans, mn = 0, 1e9
    for _, v2 in arr:
        if v2 > mn:
            continue
        mn = v2
        ans += 1

    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, arr))