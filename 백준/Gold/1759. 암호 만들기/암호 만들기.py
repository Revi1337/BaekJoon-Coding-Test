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

    def recursive(depth, index, lst):
        if depth == N:
            cnt1 = cnt2 = 0
            for alpha in lst:
                if alpha in mo:
                    cnt1 += 1
                else:
                    cnt2 += 1
            if cnt1 >= 1 and cnt2 >= 2:
                answer.append(lst)
            return
        for idx in range(index, C):
            recursive(depth + 1, idx + 1, lst + [alphas[idx]])

    answer = []
    recursive(0, 0, [])
    for ans in answer:
        print(*ans, sep = '')

N, C = map(int, input().split())
alphas = input().rstrip().split()
solution(N, C, alphas)