import sys

input = sys.stdin.readline

def solution(n, numbers, q, questions):
    answer = [0] * n
    for idx in range(n - 1):
        if numbers[idx] > numbers[idx + 1]:
            answer[idx] = 1

    prefix_sum = [0] * (n + 1)
    for idx in range(1, n + 1):
        prefix_sum[idx] = prefix_sum[idx - 1] + answer[idx - 1]

    for from_, to_ in questions:
        print(prefix_sum[to_ - 1] - prefix_sum[from_ - 1])

n = int(input().rstrip())
numbers = list(map(int, input().split()))
q = int(input().rstrip())
questions = [list(map(int, input().split())) for _ in range(q)]
solution(n, numbers, q, questions)
