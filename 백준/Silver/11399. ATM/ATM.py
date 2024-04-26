import sys

input = sys.stdin.readline

def solution(N, P):
    P.sort()
    prefix_sum = [0] * N
    prefix_sum[0] = P[0]
    for idx in range(1, N):
        prefix_sum[idx] = P[idx] + prefix_sum[idx - 1]
    return sum(prefix_sum)

N = int(input().rstrip())
P = list(map(int, input().split()))
print(solution(N, P))