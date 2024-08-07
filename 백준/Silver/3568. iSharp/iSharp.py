import sys

input = sys.stdin.readline

'''
iSharp (https://www.acmicpc.net/problem/3568)
'''

def solution(string):
    string = string.split()
    type, vars = string[0], list(map(lambda x: x[:-1], string[1:]))
    for var in vars:
        point = None
        var_len = len(var)
        for idx in range(var_len):
            if not var[idx].isalpha():
                point = idx
                break

        variable = ''
        if point is None:
            variable = var
        else:
            variable = var[:point]

        decorator = ''
        if var != variable:
            decorator = list(var[point:][::-1])

        for idx in range(len(decorator)):
            if decorator[idx] == '[':
                decorator[idx] = ']'
            elif decorator[idx] == ']':
                decorator[idx] = '['
        decorator = "".join(decorator)

        print(f'{type + decorator} {variable};')

string = input().strip()
solution(string)
