import sys

input = sys.stdin.readline

def solution(X):
    frequency = [0] * 10
    for char in str(X):
        frequency[int(char)] += 1
    sorted_x = sorted(str(X), reverse=True)
    sorted_x = int("".join(sorted_x))
    for number in range(X + 1, sorted_x + 1):
        counter = [0] * 10
        for char in str(number):
            counter[int(char)] += 1
        if counter == frequency:
            return number
        del counter
    return 0

X = int(input())
print(solution(X))
