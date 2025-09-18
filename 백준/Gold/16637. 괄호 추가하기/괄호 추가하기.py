# 2025-09-18
# https://www.acmicpc.net/problem/16637

import sys

input = sys.stdin.readline

def solution(N, exp):

    def calc(a, op, b):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b

    def backtrack(oidx, curr):
        if oidx >= len(ops):
            nonlocal mx
            mx = max(mx, curr)
            return

        nv = calc(curr, ops[oidx], nums[oidx + 1])
        backtrack(oidx + 1, nv)

        if oidx + 1 < len(ops):
            bnv = calc(nums[oidx + 1], ops[oidx + 1], nums[oidx + 2])
            nv = calc(curr, ops[oidx], bnv)
            backtrack(oidx + 2, nv)

    nums, ops = [], []
    for idx, char in enumerate(exp):
        if idx % 2 == 0:
            nums.append(int(char))
        else:
            ops.append(char)

    mx = -2 ** 31
    backtrack(0, nums[0])

    return mx

N = int(input())
exp = input().rstrip()
print(solution(N, exp))