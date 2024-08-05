import sys

input = sys.stdin.readline

'''
소수 단어 (https://www.acmicpc.net/problem/2153)
'''

def solution(string: str):
    prime = 0
    for char in string:
        if char.islower():
            prime += ord(char) - 96
        else:
            prime += ord(char) - 38
    for integer in range(2, int(prime ** 0.5) + 1):
        if not prime % integer:
            return 'It is not a prime word.'

    return 'It is a prime word.'

string = input().strip()
print(solution(string))