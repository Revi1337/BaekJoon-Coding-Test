import sys

input = sys.stdin.readline

def solution(N, M):

    def recursive(depth, lst):
        if depth == M:
            answer.append(lst)
            return
        for num in range(1, N + 1):
            if not check[num]:
                check[num] = 1
                recursive(depth + 1, lst + [num])
                check[num] = 0

    check = [0] * (N + 1)
    answer = []
    recursive(0, [])

    for line in answer:
        print(*line)

N, M = map(int, input().split())
solution(N, M)