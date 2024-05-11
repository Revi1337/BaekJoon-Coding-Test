import sys

input = sys.stdin.readline

def solution(E, S, M):
    for year in range(1, 7981):
        e1, s1, m1 = (year - E) % 15, (year - S) % 28, (year - M) % 19
        if (e1, s1, m1) == (0, 0, 0):
            return year

E, S, M = map(int, input().split())
print(solution(E, S, M))
