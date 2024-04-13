import sys

input = sys.stdin.readline

def solution(a, b, A, B):
    a = set(A)
    b = set(B)
    diff1 = a - b
    diff2 = b - a
    return len({*diff1, *diff2})

a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solution(a, b, A, B))