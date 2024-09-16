import sys

input = sys.stdin.readline

"""
부분 수열의 합 (https://www.acmicpc.net/problem/1182)
2024-09-16
"""

def solution(N, S, nums):

    def recursive(depth, max_depth, index, lst):
        if depth == max_depth:
            answer.append(lst)
            return
        for idx in range(N):
            if not check[idx] and idx >= index:
                check[idx] = 1
                recursive(depth + 1, max_depth, idx, lst + [nums[idx]])
                check[idx] = 0

    answer = []
    check = [0] * N
    for depth in range(1, N + 1):
        recursive(0, depth, 0, [])

    ans = 0
    for line in answer:
        if sum(line) == S:
            ans += 1
    print(ans)


N, S = map(int, input().split())
nums = list(map(int, input().split()))
solution(N, S, nums)

