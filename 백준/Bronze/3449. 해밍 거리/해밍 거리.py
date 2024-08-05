import sys

input = sys.stdin.readline

'''
해밍 거리 (https://www.acmicpc.net/problem/3449)
'''

def solution(one, two):
    answer = 0
    for idx in range(len(one)):
        if one[idx] != two[idx]:
            answer += 1
    print(f'Hamming distance is {answer}.')

T = int(input())
for _ in range(T):
    one = input().strip()
    two = input().strip()
    solution(one, two)
