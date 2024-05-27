import sys

input = sys.stdin.readline

def solution(N, M):

    def permutation(current):
        if len(current) == M:
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
