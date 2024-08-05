import sys

input = sys.stdin.readline

'''
팬그램 (https://www.acmicpc.net/problem/5704)
'''

def solution(words):
    for word in words:
        length = len(word) // 2
        one, two = word[:length][-1], word[length:][0]
        if one == two:
            print('Do-it')
        else:
            print('Do-it-Not')

N = int(input())
words = [input().strip() for _ in range(N)]
solution(words)