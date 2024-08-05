import sys

input = sys.stdin.readline

'''
유학 금지 (https://www.acmicpc.net/problem/2789)
'''

def solution(string):
    book = set(list('CAMBRIDGE'))
    string = list(string)
    for idx in range(len(string)):
        if string[idx] in book:
            string[idx] = ''
    return "".join(string)


string = input()
print(solution(string))
