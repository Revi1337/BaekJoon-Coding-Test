import sys
from itertools import permutations

open = sys.stdin.readline

def solution(N, A):
    perm = permutations(A)
    answer = -1e9
    for per in perm:
        tmp = 0
        for idx in range(1, N):
            tmp += abs(per[idx - 1] - per[idx])
        answer = max(answer, tmp)
    return answer

N = int(input())
A = list(map(int, input().split()))
print(solution(N, A))