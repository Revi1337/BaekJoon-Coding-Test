# 2026-03-11
# https://www.acmicpc.net/problem/3273
def solution(N, arr, X):
    sarr = set(arr)
    used = set()
    ans = 0
    for n1 in arr:
        n2 = X - n1
        if n2 in sarr and n2 not in used:
            ans += 1

    return ans // 2

N = int(input())
arr = list(map(int, input().split()))
X = int(input())
print(solution(N, arr, X))
