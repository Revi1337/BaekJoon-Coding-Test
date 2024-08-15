import sys

input = sys.stdin.readline

'''
임진왜란 (https://www.acmicpc.net/problem/3077)
2024-08-15
'''

def solution(N, answer, stu):
    total = N * (N - 1) // 2
    book = {}
    for idx in range(N):
        book[answer[idx]] = idx
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if book[stu[i]] < book[stu[j]]:
                ans += 1
    return f'{ans}/{total}'

N = int(input())
answer = input().split()
stu = input().split()
print(solution(N, answer, stu))