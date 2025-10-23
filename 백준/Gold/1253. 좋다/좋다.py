def solution(N, arr):
    arr.sort()
    ans = 0
    for idx in range(N):
        num, left, right = arr[idx], 0, N - 1
        while left < right:
            if left == idx:
                left += 1
                continue
            if right == idx:
                right -= 1
                continue

            if arr[left] + arr[right] == num:
                ans += 1
                break
            if arr[left] + arr[right] < num:
                left += 1
            else:
                right -= 1

    return ans

N = int(input())
arr = list(map(int, input().split()))
print(solution(N, arr))