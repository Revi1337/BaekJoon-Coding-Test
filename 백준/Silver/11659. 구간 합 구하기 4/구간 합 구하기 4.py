import sys

input = sys.stdin.readline

def solution(n, numbers, require):
    prefix_sum = [0] * (n + 1)
    for idx in range(1, n + 1):
        prefix_sum[idx] = prefix_sum[idx - 1] + numbers[idx - 1]

    for st, end in require:
        print(prefix_sum[end] - prefix_sum[st - 1])

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
require = [list(map(int, input().split())) for _ in range(m)]
solution(n, numbers, require)
