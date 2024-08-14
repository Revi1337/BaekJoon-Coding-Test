import sys

input = sys.stdin.readline

'''
여우는 어떻게 울지? (https://www.acmicpc.net/problem/9536)
'''

def solution(sounds, strings):
    book = set()
    for string in strings:
        for sound in string:
            book.add(sound)
    answer = []
    for sound in sounds:
        if sound not in book:
            answer.append(sound)
    return " ".join(answer)

T = int(input())
for _ in range(T):
    sounds = input().split()
    strings = []
    while True:
        string = input().rstrip()
        if string == 'what does the fox say?':
            break
        strings.append(string.split())
    print(solution(sounds, strings))

