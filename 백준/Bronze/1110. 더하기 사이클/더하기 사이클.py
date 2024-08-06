import sys

input = sys.stdin.readline

'''
더하기 사이클 (https://www.acmicpc.net/problem/1032)
'''

def solution(N):
    num = N
    cache = set()
    answer = 0
    while True:
        cache.add(num)
        answer += 1
        original = num
        if len(original) < 2:
            num = num + '0'
        new = sum([int(val) for val in num])
        num = str(int(original[-1] + str(new)[-1]))
        if num in cache:
            break

    return answer

N = input().rstrip()
print(solution(N))