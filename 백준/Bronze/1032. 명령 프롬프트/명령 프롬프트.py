import sys

input = sys.stdin.readline

'''
명령 프롬프트 (https://www.acmicpc.net/problem/1032)
'''

def solution(s, strings):
    diff = []
    for idx in range(len(strings[0])):
        book = [strings[0][idx]] * s
        entry = [string[idx] for string in strings]
        if book == entry:
            diff.append(strings[0][idx])
        else:
            diff.append('?')
    return "".join(diff)

s = int(input())
strings = [input().rstrip() for _ in range(s)]
print(solution(s, strings))
