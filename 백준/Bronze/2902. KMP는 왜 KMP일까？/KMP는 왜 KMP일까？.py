import sys

input = sys.stdin.readline

'''
KMP 는 왜 KMP일까? (https://www.acmicpc.net/problem/2902)
'''

def solution(string):
    return "".join(map(lambda s: s[0], string.split('-')))

string = input()
print(solution(string))
