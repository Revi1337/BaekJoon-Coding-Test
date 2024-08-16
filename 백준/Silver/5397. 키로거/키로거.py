import sys

input = sys.stdin.readline

'''
키로거 (https://www.acmicpc.net/problem/5397)
2024-08-16
'''

def solution(T, L):
    for case in range(T):
        string = L[case]
        slength = len(string)
        stack, cache = [[] for _ in range(2)]
        for idx in range(slength):
            if string[idx] == '<':
                if stack:
                    cache.append(stack.pop())
            elif string[idx] == '>':
                if cache:
                    stack.append(cache.pop())
            elif string[idx] == '-':
                if stack:
                    stack.pop()
            else:
                stack.append(string[idx])
        stack.extend(cache[::-1])
        print(*stack, sep = '')

T = int(input())
L = [input().rstrip() for _ in range(T)]
solution(T, L)
