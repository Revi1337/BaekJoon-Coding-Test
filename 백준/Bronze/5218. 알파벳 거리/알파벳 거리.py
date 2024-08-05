import sys

input = sys.stdin.readline

'''
알파벳 거리 (https://www.acmicpc.net/problem/5218)
'''

def solution(words):
    for word1, word2 in words:
        print('Distances: ', end = '')
        for idx in range(len(word1)):
            x, y = ord(word1[idx]), ord(word2[idx])
            if y >= x:
                print(y - x, end = ' ')
            else:
                print(y + 26 - x, end = ' ')
        print()

T = int(input())
words = [input().split() for _ in range(T)]
solution(words)