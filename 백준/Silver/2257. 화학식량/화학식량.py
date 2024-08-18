import sys

input = sys.stdin.readline

'''
화학식량 (https://www.acmicpc.net/problem/2257)
2024-08-18
'''

def solution(string):
    kdict = {'C': 12, 'H': 1, 'O': 16}
    stack = []
    for idx in range(len(string)):
        if string[idx] == '(':
            stack.append(string[idx])
        elif string[idx] in ['C', 'H', 'O']:
            stack.append(kdict[string[idx]])
        elif string[idx].isdigit():
            stack.append(stack.pop() * int(string[idx]))
        else:
            temp = 0
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(temp)
                    break
                else:
                    temp += stack.pop()
    return sum(stack)

string = input().rstrip()
print(solution(string))
