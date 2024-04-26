import sys

input = sys.stdin.readline

def solution(N, X):
    sorted_x = sorted(X)
    prefix_sum = {sorted_x[0]: 0}
    for idx in range(N):
        prefix_sum[sorted_x[idx]] = prefix_sum.get(sorted_x[idx])
        if sorted_x[idx] > sorted_x[idx - 1]:
            prefix_sum[sorted_x[idx]] = prefix_sum[sorted_x[idx - 1]] + 1

    for x in X:
        print(prefix_sum[x], end = ' ')

N = int(input().rstrip())
X = list(map(int, input().split()))
solution(N, X)
