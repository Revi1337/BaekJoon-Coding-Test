import sys

def solution(words):
    words = set(words)
    words = sorted(words, key=lambda x: (len(x), x))
    for word in words:
        print(word)

input = sys.stdin.readline
loop = int(input())
words = [input().rstrip() for _ in range(loop)]
solution(words)