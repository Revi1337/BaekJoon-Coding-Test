def solution(N, M, A):
    answer = left = right = 0
    sm = A[0]

    while left < N:
        if sm < M and right + 1 < N:
            right += 1
            sm += A[right]
        else:
            if sm == M:
                answer += 1
            sm -= A[left]
            left += 1

    return answer

N, M = map(int, input().split())
A = list(map(int, input().split()))
print(solution(N, M, A))
