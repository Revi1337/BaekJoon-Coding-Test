import sys

input = sys.stdin.readline

def solution(N, K, arr):
    arr.sort()
    ans, left, right = 0, 0, N - 1
    while left < right:
        if arr[left] + arr[right] <= K:
            ans += 1
            left, right = left + 1, right - 1
        else:
            right -= 1

    return ans

N, K = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
print(solution(N, K, arr))