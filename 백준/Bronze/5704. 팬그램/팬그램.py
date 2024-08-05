import sys

input = sys.stdin.readline

'''
JOI와 IOI (https://www.acmicpc.net/problem/5586)
'''

def solution(lines):
    for line in lines:
        dat = [0] * 26
        for char in line:
            if char != ' ' and not dat[ord(char) - 97]:
                dat[ord(char) - 97] += 1
        if sum(dat) == 26:
            print('Y')
        else:
            print('N')

lines = []
while True:
    line = input().strip()
    if line == '*':
        break
    lines.append(line)
solution(lines)