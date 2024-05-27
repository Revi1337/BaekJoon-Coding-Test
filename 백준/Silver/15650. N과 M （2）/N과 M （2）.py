import sys

input = sys.stdin.readline


def solution(N, M):

    def permutation(current):
        if len(current) == M:
            prev = current[0]
            breaked = False
            for idx in range(1, M):
                if current[idx] < prev:
                    breaked = True
                    break
                prev = current[idx]
            if not breaked:
                answer.append(current[:])
            return
        for number in range(1, N + 1):
            if number not in current:
                current.append(number)
                permutation(current)
                current.pop()

    answer = []
    permutation([])
    for line in answer:
        print(*line)

N, M = map(int, input().split())
solution(N, M)
