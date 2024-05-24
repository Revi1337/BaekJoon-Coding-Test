import sys
from collections import Counter

input = sys.stdin.readline

def solution(X):
    frequency = Counter(str(X))
    sorted_x = sorted(str(X), reverse=True)
    sorted_x = int("".join(sorted_x))
    for number in range(X + 1, sorted_x + 1):
        counter = Counter(str(number))
        if counter == frequency:
            return number
    return 0

X = int(input())
print(solution(X))