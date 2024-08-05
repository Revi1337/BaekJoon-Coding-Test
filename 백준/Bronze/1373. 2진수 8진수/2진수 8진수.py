import sys

input = sys.stdin.readline

def solution(binary):
    return oct(int(binary, 2))[2:]

binary = input().strip()
print(solution(binary))