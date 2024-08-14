import sys

input = sys.stdin.readline

'''
수열 (https://www.acmicpc.net/problem/2559)
2024-08-14
'''

def solution(N, K, temps):
    left, right = 0, K
    temp = sum(temps[left : right])
    answer = temp
    while right < N:
        temp = temp - temps[left] + temps[right]
        answer = max(answer, temp)
        left, right = left + 1, right + 1
    return answer

N, K = map(int, input().split())
temps = list(map(int, input().split()))
print(solution(N, K, temps))
