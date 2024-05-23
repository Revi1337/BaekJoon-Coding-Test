import sys
from itertools import permutations

open = sys.stdin.readline

def solution(N, K, A):
    days = {day: A[day - 1] for day in range(1, N + 1)}
    answer = 0
    tmp = permutations(days.keys())
    weight = 500
    for line in tmp:
        target = weight
        fail = False
        for day in line:
            target += days[day] - K
            if target < weight:
                fail = True
                break
        if not fail:
            answer += 1
    return answer

N, K = map(int, input().split())
A = list(map(int, input().split()))
print(solution(N, K, A))