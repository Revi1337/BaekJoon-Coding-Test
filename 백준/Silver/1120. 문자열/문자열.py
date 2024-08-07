import sys

input = sys.stdin.readline

'''
문자열 (https://www.acmicpc.net/problem/1120)
'''

def solution(strings):
    answer = 1e9
    for idx in range(len(strings[1]) - len(strings[0]) + 1):
        count = 0
        for j in range(len(strings[0])):
            if strings[0][j] != strings[1][idx + j]:
                count += 1
        answer = min(answer, count)

    return answer if answer != 1e9 else 0

strings = input().split()
print(solution(strings))