import sys

input = sys.stdin.readline

'''
뒤집힌 덧셈 (https://www.acmicpc.net/problem/1357)
'''

def solution(strings):
    return int(str(int(strings[0][::-1]) + int(strings[1][::-1]))[::-1])

strings = input().strip().split()
print(solution(strings))