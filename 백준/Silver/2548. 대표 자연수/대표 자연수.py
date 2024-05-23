import sys

open = sys.stdin.readline

def solution(N, A):
    A.sort()
    total = sum([number - A[0] for number in A])
    answer = A[0]
    for idx in range(1, N):
        height = A[idx] - A[idx - 1]
        left = height * idx
        right = height * (N - idx)
        if total + left - right < total:
            answer = A[idx]
            total = total + left - right
    return answer

N = int(input())
A = list(map(int, input().split()))
print(solution(N, A))