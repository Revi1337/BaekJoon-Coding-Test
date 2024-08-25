import sys

input = sys.stdin.readline

"""
오큰수 (https://www.acmicpc.net/problem/17298)
2024-08-25
"""

def solution(N, numbers):
    stack = []
    pri = [-1] * N
    for idx in range(N):
        while stack and numbers[stack[-1]] < numbers[idx]:
            pri[stack.pop()] = numbers[idx]
        stack.append(idx)
    print(*pri)

N = int(input())
numbers = list(map(int, input().split()))
solution(N, numbers)
