import sys

input = sys.stdin.readline

'''
도비의 영어 공부 (https://www.acmicpc.net/problem/2386)
'''

def solution(strings):
    for line in strings:
        t, word = line[0], line[2:].lower()
        counter = 0
        for char in word:
            if char == t:
                counter += 1
        print(f'{t} {counter}')

strings = []
while True:
    string = input().strip()
    if string == '#':
        break
    strings.append(string)
solution(strings)


