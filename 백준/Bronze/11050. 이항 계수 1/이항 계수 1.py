import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

def solution(n, k):

    def factorial(number):
        if number == 1 or number == 0:
            return 1
        return number * factorial(number - 1)

    return factorial(n) // (factorial(k) * factorial(n - k))

n, k = map(int, input().split())
print(solution(n, k))
