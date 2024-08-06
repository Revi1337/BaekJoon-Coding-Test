import sys

input = sys.stdin.readline

'''
개표 (https://www.acmicpc.net/problem/10102)
'''

def solution(N, data):
    dat = [0] * 2
    for char in data:
        dat[ord(char) - 65] += 1

    if dat[0] > dat[1]:
        return 'A'
    if dat[1] > dat[0]:
        return 'B'
    return 'Tie'

N = int(input())
data = input().rstrip()
print(solution(N, data))