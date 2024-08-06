import sys

input = sys.stdin.readline

'''
유진수 (https://www.acmicpc.net/problem/1356)
'''

def solution(string):
    length = len(string)
    future = []
    for idx in range(1, length):
        one = string[:idx]
        two = string[idx:]
        future.append(f'{one}-{two}')

    answer = False
    for string in future:
        pre, post = string.split('-')
        ans1 = ans2 = 1
        for char in pre:
            ans1 *= int(char)
        for char in post:
            ans2 *= int(char)
        if ans1 == ans2:
            answer = True
            break

    return 'YES' if answer else 'NO'

string = input().strip()
print(solution(string))