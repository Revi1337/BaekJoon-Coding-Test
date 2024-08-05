import sys

input = sys.stdin.readline

'''
카이사르 암호 (https://www.acmicpc.net/problem/5598)
'''

def solution(word):
    answer = ''
    for char in word:
        answer += chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
    return answer

word = input().rstrip()
print(solution(word))
