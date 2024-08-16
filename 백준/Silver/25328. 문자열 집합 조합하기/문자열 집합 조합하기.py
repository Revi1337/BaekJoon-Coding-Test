import sys
from itertools import combinations

input = sys.stdin.readline

'''
문자열 집합 조합하기 (https://www.acmicpc.net/problem/25328)
2024-08-15
'''

def solution(X, Y, Z, k):
    freq = {}
    for val in combinations(list(X), k):
        freq[val] = freq.get(val, 0) + 1
    for val in combinations(list(Y), k):
        freq[val] = freq.get(val, 0) + 1
    for val in combinations(list(Z), k):
        freq[val] = freq.get(val, 0) + 1
    pre = list(filter(lambda key: freq[key] >= 2, freq.keys()))
    if not pre:
        print(-1)
        return
    answer = sorted(pre)
    for ans in answer:
        print(*ans, sep = '')

X = input().rstrip()
Y = input().rstrip()
Z = input().rstrip()
k = int(input())
solution(X, Y, Z, k)

