import sys

input = sys.stdin.readline

def solution(n, numbers, m, question):
    prefix_sum = [0] * (n + 1)
    for idx in range(1, n + 1):
        prefix_sum[idx] = prefix_sum[idx - 1] + numbers[idx - 1]

    for from_, to_ in question:
        print(prefix_sum[to_] - prefix_sum[from_ - 1])

n = int(input().rstrip())
numbers = list(map(int, input().split()))
m = int(input().rstrip())
question = [list(map(int, input().split())) for _ in range(m)]
solution(n, numbers, m, question)
