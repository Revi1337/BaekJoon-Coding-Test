import sys

input = sys.stdin.readline
def solution(n, m, cds1, cds2):
    min_length, max_length = min(n, m), max(n, m)
    total = [0] * max_length
    for idx in range(min_length):
        total[idx] = cds1[idx] + cds2[idx]
    for idx in range(min_length, max_length):
        if min_length == n:
            total[idx] = cds2[idx]
        else:
            total[idx] = cds1[idx]

    min_set = None
    answer = 0
    if min_length == n:
        min_set = set(cds1)
    else:
        min_set = set(cds2)
    for idx in range(max_length):
        if max_length == n:
            left = total[idx] - cds1[idx]
        else:
            left = total[idx] - cds2[idx]
        if left in min_set:
            answer += 1

    return answer

while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    cds1 = [int(input().rstrip()) for _ in range(n)]
    cds2 = [int(input().rstrip()) for _ in range(m)]
    print(solution(n, m, cds1, cds2))