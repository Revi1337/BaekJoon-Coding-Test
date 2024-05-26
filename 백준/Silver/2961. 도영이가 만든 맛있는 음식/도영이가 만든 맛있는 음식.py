import sys
from itertools import combinations

input = sys.stdin.readline

def solution(N, A):
    indexs, sours, bitts = [], [], []
    for idx in range(N):
        sours.append(A[idx][0])
        bitts.append(A[idx][1])
        indexs.append(idx)

    perms = []
    for length in range(1, N + 1):
        perms.extend(list(combinations(indexs, length)))

    answer = 1e9
    for perm in perms:
        tmp1, tmp2 = 1, 0
        for recipe in perm:
            tmp1 *= sours[recipe]
            tmp2 += bitts[recipe]
        answer = min(answer, abs(tmp1 - tmp2))

    return answer

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, A))
