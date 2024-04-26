import sys

input = sys.stdin.readline

def solution(T, NS):
    for N in NS:
        a, b = 1, 0
        for v in range(N):
            a, b = b, a + b
        print(a, b)

T = int(input().rstrip())
NS = [int(input().rstrip()) for _ in range(T)]
solution(T, NS)