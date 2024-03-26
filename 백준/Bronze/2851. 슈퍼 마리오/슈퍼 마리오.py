import sys

input = sys.stdin.readline

def solution(n, scores):
    prefix_sum = [0] * n
    prefix_sum[0] = scores[0]
    for idx in range(1, n):
        prefix_sum[idx] = prefix_sum[idx - 1] + scores[idx]
        if prefix_sum[idx] >= 100:
            min1 = abs(100 - prefix_sum[idx])
            min2 = abs(100 - prefix_sum[idx - 1])
            if min1 <= min2:
                return prefix_sum[idx]
            return prefix_sum[idx - 1]
    return prefix_sum[-1]

scores = [int(input().rstrip()) for _ in range(10)]
print(solution(10, scores))