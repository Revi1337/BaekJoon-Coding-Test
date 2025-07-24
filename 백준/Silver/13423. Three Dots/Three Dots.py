def solution(T, N, arr):
    arr.sort()
    cache = set(arr)
    ans = 0
    for left in range(N):
        for mid in range(left + 1, N):
            right = arr[mid] + (arr[mid] - arr[left])
            if right in cache:
                ans += 1

    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(solution(T, N, arr))