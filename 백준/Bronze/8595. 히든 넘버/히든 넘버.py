import sys

input = sys.stdin.readline

'''
히든 넘버 (https://www.acmicpc.net/problem/8595)
'''

def solution(n, string):
    answer = 0
    tmp = ''
    for idx in range(n):
        if string[idx].isdigit():
            tmp += string[idx]
        elif tmp != '':
            answer += int(tmp)
            tmp = ''
    if tmp != '':
        answer += int(tmp)

    return answer if answer else 0

n = int(input())
string = input().strip()
print(solution(n, string))