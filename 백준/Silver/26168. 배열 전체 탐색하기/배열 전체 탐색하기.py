def solution(N, M, A, B):

    def lower_bound(k):
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            if A[mid] < k:
                left = mid + 1
            else:
                right = mid
        return 0 if right == N else N - right

    def upper_bound(k):
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            if A[mid] <= k:
                left = mid + 1
            else:
                right = mid
        return 0 if right == N else N - right

    def bisect(i, j):
        return lower_bound(i) - upper_bound(j)

    A.sort()
    for ques in B:
        if ques[0] == 1:
            print(lower_bound(ques[1]))
        elif ques[0] == 2:
            print(upper_bound(ques[1]))
        else:
            print(bisect(ques[1], ques[2]))

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, A, B)