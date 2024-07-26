import sys

input = sys.stdin.readline

def solution(N, targets):
    targets.insert(0, 0)
    curr = 1
    cache = [0] * (N + 1)
    answer = 0
    while cache[N] != 1:
        if cache[targets[curr]]:
            return 0
        curr = targets[curr]
        cache[curr] = 1
        answer += 1

    return answer

T = int(input())
for _ in range(T):
    N = int(input())
    targets = [int(input()) for _ in range(N)]
    print(solution(N, targets))