import sys

input = sys.stdin.readline

'''
파일 완전 삭제 (https://www.acmicpc.net/problem/9243)
'''

def solution(N, data1, data2):
    if N % 2:
        data1 = list(data1)
        string = []
        for char in data1:
            integer = int(char)
            if integer:
                integer = 0
            else:
                integer = 1
            string.append(str(integer))
        if "".join(string) == data2:
            return 'Deletion succeeded'
        return 'Deletion failed'
    if data1 == data2:
        return 'Deletion succeeded'
    return 'Deletion failed'

N = int(input())
data1 = input().rstrip()
data2 = input().rstrip()
print(solution(N, data1, data2))