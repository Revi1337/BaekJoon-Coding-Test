import sys

input = sys.stdin.readline

def solution(n, m, N, M):
    N = set(N)
    answer = 0
    for string in M:
        if string in N:
            answer += 1
    return answer

n, m = map(int, input().split())
N = [input() for _ in range(n)]
M = [input() for _ in range(m)]
print(solution(n, m, N, M))