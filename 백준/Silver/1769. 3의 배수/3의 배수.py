import sys

input = sys.stdin.readline

'''
3의 배수 (https://www.acmicpc.net/problem/1769) 
'''

def solution(N):
    answer = 0
    N = str(N)
    while len(N) > 1:
        N = str(sum([int(char) for char in str(N)]))
        answer += 1

    print(answer)
    print('YES' if not int(N) % 3 else 'NO')

N = int(input())
solution(N)
