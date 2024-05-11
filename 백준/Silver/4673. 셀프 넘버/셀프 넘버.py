import sys

input = sys.stdin.readline

def solution():
    integers = [1] * (10001)
    for integer in range(1, 10001):
        sumN = sum(map(int, str(integer))) + integer
        if sumN <= 10000:
            integers[sumN] = 0

    for num, val in enumerate(integers[1:], start=1):
        if val:
            print(num)

solution()