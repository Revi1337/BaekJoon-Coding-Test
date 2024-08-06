import sys

input = sys.stdin.readline

'''
Serious Problem (https://www.acmicpc.net/problem/17094)
'''

def solution(s, string):
    dat = [0] * 52
    for char in string:
        dat[ord(char) - 50] += 1

    if dat[0] > dat[-1]:
        return '2'
    if dat[0] < dat[-1]:
        return 'e'
    return 'yee'

s = input()
string = input().rstrip()
print(solution(s, string))
