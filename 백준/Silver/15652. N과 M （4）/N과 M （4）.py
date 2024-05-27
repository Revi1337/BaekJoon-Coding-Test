import sys

input = sys.stdin.readline

def solution(N, M):

    def permutation(current):
        if len(current) == M:
            for idx in range(1, M):
                if current[idx] < current[idx - 1]:
                    break
            else:
                answer.append(current[:])
            return
        for number in range(1, N + 1):
            current.append(number)
            permutation(current)
            current.pop()

    answer = []
    permutation([])
    for line in answer:
        print(*line)

N, M = map(int, input().split())
solution(N, M)
