import sys

input = sys.stdin.readline

def solution(N, A):
    for idx in range(N - 1, 0, -1):
        if A[idx - 1] > A[idx]:
            target = idx - 1
            break
    else:
        print(-1)
        return

    for idx in range(N - 1, 0, -1):
        if A[idx] < A[target]:
            A[idx], A[target] = A[target], A[idx]
            break
    answer = A[:target + 1] + sorted(A[target + 1:], reverse=True)
    print(*answer)

N = int(input())
A = list(map(int, input().split()))
solution(N, A)