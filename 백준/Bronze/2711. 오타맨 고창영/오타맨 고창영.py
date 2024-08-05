import sys

input = sys.stdin.readline

'''
오타맨 고창영 (https://www.acmicpc.net/problem/2711)
'''

def solution(lines):
    for idx, word in lines:
        idx = int(idx) - 1
        word = list(word)
        word[idx] = ''
        print("".join(word))

T = int(input())
lines = [input().strip().split() for _ in range(T)]
solution(lines)
