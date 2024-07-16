import sys

input = sys.stdin.readline

def solution(N, K, data):
    curr = 0
    cache = [0] * N
    answer = 0
    while cache[K] != 1:
        if cache[data[curr]]:
            return -1
        curr = data[curr]
        cache[curr] = 1
        answer += 1

    return answer

N, K = map(int, input().split())
data = [int(input()) for _ in range(N)]
print(solution(N, K, data))
