import sys

input = sys.stdin.readline

'''
애너그램 (https://www.acmicpc.net/problem/6996)
'''

def solution(N, lines):
    for v1, v2 in lines:
        d1, d2 = dict(), dict()
        for char in v1:
            d1[char] = d1.get(char, 0) + 1
        for char in v2:
            d2[char] = d2.get(char, 0) + 1
        if d1 == d2:
            print(f'{v1} & {v2} are anagrams.')
        else:
            print(f'{v1} & {v2} are NOT anagrams.')

N = int(input())
lines = [input().split() for _ in range(N)]
solution(N, lines)