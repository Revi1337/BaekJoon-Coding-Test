def solution(N, A, M, B):
    B.sort()
    total = 0

    for idx in range(N):
        curr = A[idx]
        left, right = 0, M - 1
        clo = B[0]

        while left <= right:
            mid = (left + right) // 2
            if abs(B[mid] - curr) < abs(clo - curr) or (abs(B[mid] - curr) == abs(clo - curr) and B[mid] < clo):
                clo = B[mid]
            if B[mid] < curr:
                left = mid + 1
            else:
                right = mid - 1

        total += clo

    return total

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solution(N, A, M, B))