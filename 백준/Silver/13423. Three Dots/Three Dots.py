def solution(T, N, arr):
    arr.sort()
    ans = 0
    for idx in range(N):
        for jdx in range(idx + 1, N):
            diff = arr[jdx] - arr[idx]
            left, right = jdx + 1, N - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] - arr[jdx] == diff:
                    ans += 1
                if arr[mid] - arr[jdx] < diff:
                    left = mid + 1
                else:
                    right = mid - 1
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(solution(T, N, arr))