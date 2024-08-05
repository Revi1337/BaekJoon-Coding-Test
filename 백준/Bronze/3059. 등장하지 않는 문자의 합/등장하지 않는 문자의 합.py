import sys

input = sys.stdin.readline

'''
등장하지 않는 문자의 합 (https://www.acmicpc.net/problem/3059)
'''

def solution(strings):
    for string in strings:
        dat = [1] * 26
        answer = 0
        for char in string:
            dat[ord(char) - 65] -= 1
        for idx in range(26):
            if dat[idx] == 1:
                answer += 65 + idx
        print(answer)


T = int(input())
strings = [input().strip() for _ in range(T)]
solution(strings)
