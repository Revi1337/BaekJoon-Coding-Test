import sys

input = sys.stdin.readline

'''
넷이 놀기 (https://www.acmicpc.net/problem/2121)
2024-08-15
'''

def solution(N, A, B, posi):
    answer = 0
    for col, row in posi:
        if (col, row + B) in posi and (col + A, row) in posi and (col + A, row + B) in posi:
            answer += 1
    return answer

N = int(input())
A, B = map(int, input().split())
posi = set()
for _ in range(N):
    posi.add(tuple(map(int, input().split())))
print(solution(N, A, B, posi))