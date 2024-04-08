import sys

input = sys.stdin.readline

def solution(n, x, days):
    answer = sum(days[:x])
    total = answer
    counter = 1
    for idx in range(x, n):
        total -= days[idx - x]
        total += days[idx]
        if total > answer:
            answer = total
            counter = 1
        elif total == answer:
            counter += 1

    if answer == 0:
        print('SAD')
    else:
        print(answer)
        print(counter)

n, x = map(int, input().split())
days = list(map(int, input().split()))
solution(n, x, days)
