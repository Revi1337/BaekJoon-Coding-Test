import sys

input = sys.stdin.readline

'''
니모를 찾아서 (https://www.acmicpc.net/problem/10173)
'''

def solution(lines):
    for line in lines:
        string = ''
        for char in line:
            if char.isalpha():
                string += char
            else:
                if string.lower() == 'nemo':
                    print('Found')
                    break
                string = ''
        else:
            print('Missing')

lines = []
while True:
    line = input().rstrip()
    if line == 'EOI':
        break
    lines.append(line)
solution(lines)