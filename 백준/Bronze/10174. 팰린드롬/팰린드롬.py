'''
팰린드롬 (https://www.acmicpc.net/problem/10174)
'''

def solution(N, words):
    for word in words:
        word = word.lower()
        if word[::-1] == word:
            print('Yes')
        else:
            print('No')

N = int(input())
words = [input() for _ in range(N)]
solution(N, words)