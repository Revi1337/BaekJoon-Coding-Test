import sys

input = sys.stdin.readline

def solution(N, M, A, K, B):
    answer = [[0] * K for _ in range(N)]
    for n in range(N):
        for k in range(K):
            for m in range(M):
                answer[n][k] += A[n][m] * B[m][k]

    for v in answer:
        print(*v)

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
_, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, A, K, B)
