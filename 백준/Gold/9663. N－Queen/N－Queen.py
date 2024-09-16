import sys

input = sys.stdin.readline

"""
N-Queen (https://www.acmicpc.net/problem/9663)
2024-09-16
"""

def solution(N):

    def recursive(depth):
        if depth == N:
            nonlocal answer
            answer += 1
            return
        for nc in range(N):
            if check1[nc] == check2[depth + nc] == check3[depth - nc] == 0:
                check1[nc] = check2[depth + nc] = check3[depth - nc] = 1
                recursive(depth + 1)
                check1[nc] = check2[depth + nc] = check3[depth - nc] = 0

    answer = 0
    check1 = [0] * N
    check2, check3 = [[0] * (2 * N) for _ in range(2)]
    recursive(0)
    print(answer)

N = int(input())
solution(N)