# 2026-03-13
# https://www.acmicpc.net/problem/1931
# greedy

def solution(N, arr):
    arr.sort(key=lambda x: (x[1], x[0]))
    ans = cend = 0
    for st, end in arr:
        if st >= cend:
            cend = end
            ans += 1

    return ans

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))