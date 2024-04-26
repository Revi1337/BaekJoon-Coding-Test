import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def solution(N):
    if N == 0:
        return 1

    def recursive(N):
        if N == 1:
            return 1
        return N * recursive(N - 1)

    return recursive(N)

N = int(input().rstrip())
print(solution(N))

