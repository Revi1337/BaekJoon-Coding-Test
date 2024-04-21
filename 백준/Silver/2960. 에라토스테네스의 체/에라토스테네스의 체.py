import sys

input = sys.stdin.readline

def solution(N, K):
    integers = [1] * (N + 1)
    counter = 0
    for integer in range(2, N + 1):
        for padding in range(integer, N + 1, integer):
            if integers[padding]:
                integers[padding] = 0
                counter += 1
                if counter == K:
                    return padding

N, K = map(int, input().split())
print(solution(N, K))
