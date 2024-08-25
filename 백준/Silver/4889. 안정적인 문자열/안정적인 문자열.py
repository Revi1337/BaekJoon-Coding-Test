import sys

input = sys.stdin.readline

"""
안정적인 문자열 (https://www.acmicpc.net/problem/4889)
2024-08-20
"""

def solution(words):
    for idx, word in enumerate(words, start=1):
        stack = []
        answer = 0
        for char in word:
            if char == '{':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    answer += 1
                    stack.append('{')
        answer += len(stack) // 2
        print(f'{idx}. {answer}')

words = []
while True:
    word = input().rstrip()
    if '-' in word:
        break
    words.append(word)
solution(words)
