def solution(N, M, arr):
    arr.sort()
    left = right = 0
    answer = max(arr) - min(arr)
    while left <= right < N:
        if abs(arr[left] - arr[right]) >= M:
            answer = min(answer, abs(arr[left] - arr[right]))
            left += 1
        else:
            right += 1

    return answer

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
print(solution(N, M, arr))