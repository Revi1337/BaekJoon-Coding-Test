import sys

input = sys.stdin.readline

'''
도비의 난독증 테스트 (https://www.acmicpc.net/problem/2204)
'''

def solution(n, words):
    s_words = sorted(words, key = lambda x: x.lower())
    return s_words[0]

while True:
    n = input()
    if int(n) == 0:
        break
    words = [input().strip() for _ in range(int(n))]
    print(solution(n, words))