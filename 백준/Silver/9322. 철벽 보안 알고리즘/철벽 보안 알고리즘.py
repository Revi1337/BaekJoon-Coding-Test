import sys

input = sys.stdin.readline

'''
철벽 보안 알고리즘 (https://www.acmicpc.net/problem/9322)
'''

def solution(n, one, two, ciphertext):
    offsets = []
    for word in two:
        for idx in range(n):
            if one[idx] == word:
                offsets.append(idx)

    answer = [0] * n
    for idx in range(n):
        answer[offsets[idx]] = ciphertext[idx]

    return " ".join(answer)

T = int(input())
for _ in range(T):
    n = int(input())
    one = input().split()
    two = input().split()
    ciphertext = input().split()
    print(solution(n, one, two, ciphertext))

