import sys

input = sys.stdin.readline

"""
부분 수열의 합 (https://www.acmicpc.net/problem/1182)
2024-09-16
"""

def solution(N, S, nums):

    def recursive(index, sm, cnt):
        if index == N:
            if cnt and sm == S:
                nonlocal answer
                answer += 1
            return
        recursive(index + 1, sm + nums[index], cnt + 1)
        recursive(index + 1, sm, cnt)

    answer = 0
    recursive(0, 0, 0)
    print(answer)

N, S = map(int, input().split())
nums = list(map(int, input().split()))
solution(N, S, nums)


