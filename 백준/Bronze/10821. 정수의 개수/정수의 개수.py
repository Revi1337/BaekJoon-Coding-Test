import sys

input = sys.stdin.readline

'''
정수의 개수 (https://www.acmicpc.net/problem/10821)
'''

def solution(string):
    return len(list(filter(lambda x: x.isdecimal(), string.split(','))))

string = input().rstrip()
print(solution(string))