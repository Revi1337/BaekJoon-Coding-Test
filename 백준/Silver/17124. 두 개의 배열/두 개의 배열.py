def solution(N, A, M, B):
    B.sort()
    total = 0

    for num in A:
        left, right = 0, M - 1
        while left < right:
            mid = (left + right) // 2
            if B[mid] <= num:
                left = mid + 1
            else:
                right = mid

        if left == 0:
            total += B[left]
        else:
            if num - B[left - 1] > B[left] - num:
                total += B[left]
            else:
                total += B[left - 1]

    return total

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solution(N, A, M, B))