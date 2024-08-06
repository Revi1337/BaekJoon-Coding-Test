import sys

input = sys.stdin.readline

'''
민균이의 비밀번호 (https://www.acmicpc.net/problem/9933)
'''

def solution(N, words):
    book = set(words)
    for word in words:
        book.discard(word)
        if word[::-1] in book or word[::-1] == word:
            length = len(word)
            print(f'{length} {word[length // 2]}')
            break
        book.add(word)

N = int(input())
words = [input().rstrip() for _ in range(N)]
solution(N, words)