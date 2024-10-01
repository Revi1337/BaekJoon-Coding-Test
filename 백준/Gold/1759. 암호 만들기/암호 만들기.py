import sys

input = sys.stdin.readline

"""
암호 만들기 (https://www.acmicpc.net/problem/1759)
2024-09-29
"""

'''
중요 조건 
1. 최소 한개의 모음과 최소 두개의 자음.
2. 알파벳은 오름차순으로
'''

mo = {'a', 'e', 'i', 'o', 'u'}

def solution(N, C, alphas):
    alphas.sort()

    def recursive(n, cnt, lst):
        if n == C:
            if len(lst) == N and cnt >= 1 and N - cnt >= 2:
                answer.append(lst)
            return
        if alphas[n] in mo:
            recursive(n + 1, cnt + 1, lst + [alphas[n]])
        else:
            recursive(n + 1, cnt, lst + [alphas[n]])
        recursive(n + 1, cnt, lst)

    answer = []
    recursive(0, 0, [])
    for ans in answer:
        print(*ans, sep = '')

N, C = map(int, input().split())
alphas = input().rstrip().split()
solution(N, C, alphas)
