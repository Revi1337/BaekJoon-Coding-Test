import sys

input = sys.stdin.readline

'''
철벽 보안 알고리즘 (https://www.acmicpc.net/problem/9322)
'''

def solution(string):

    def gcd(num1, num2):
        min_num, max_num = min(num1, num2), max(num1, num2)
        while max_num % min_num > 0:
            max_num, min_num = min_num, max_num % min_num
        return min_num

    integer = gcd(string[0], string[1])
    return f'{string[0] // integer}:{string[1] // integer}'


string = list(map(int, input().split(':')))
print(solution(string))
