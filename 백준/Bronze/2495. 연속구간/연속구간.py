import sys

input = sys.stdin.readline

'''
연속구간 (https://www.acmicpc.net/problem/2495)
'''

def solution(integers):
    for integer in integers:
        answer = counter = 1
        length = len(integer)
        for idx in range(1, length):
            if integer[idx] == integer[idx - 1]:
                counter += 1
            else:
                answer = max(answer, counter)
                counter = 1
        answer = max(answer, counter)
        print(answer)

integers = [input().strip() for _ in range(3)]
solution(integers)