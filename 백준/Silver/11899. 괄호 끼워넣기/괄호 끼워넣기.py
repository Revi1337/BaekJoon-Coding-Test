import sys

input = sys.stdin.readline

'''
괄호 끼워넣기 (https://www.acmicpc.net/problem/11899)
'''

def solution(S):
    stack = []
    for char in S:
        if char == '(':
            stack.append(char)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)

    return len(stack)

S = input().rstrip()
print(solution(S))