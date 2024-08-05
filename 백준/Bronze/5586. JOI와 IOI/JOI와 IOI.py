import sys

input = sys.stdin.readline

'''
JOI와 IOI (https://www.acmicpc.net/problem/5586)
'''

def solution(string):
    answer = [0, 0]
    for idx in range(len(string) - 2):
        if string[idx : idx + 3] == 'JOI':
            answer[0] += 1
        elif string[idx: idx + 3] == 'IOI':
            answer[1] += 1
    print(*answer, sep = '\n')

string = input().strip()
solution(string)
