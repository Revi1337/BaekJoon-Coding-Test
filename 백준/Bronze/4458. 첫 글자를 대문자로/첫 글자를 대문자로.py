import sys

input = sys.stdin.readline

'''
첫 글자를 대문자로 (https://www.acmicpc.net/problem/4458)
'''

def solution(N, lines):
    for line in lines:
        print(line[0].upper() + line[1:])

N = int(input())
lines = [input().strip() for _ in range(N)]
solution(N, lines)