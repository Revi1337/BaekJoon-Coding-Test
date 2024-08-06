import sys

input = sys.stdin.readline

'''
첼시를 도와줘 (https://www.acmicpc.net/problem/11098)
'''

def solution(p, datas):
    datas = sorted(datas, key = lambda x: -int(x[0]))
    return datas[0][1]

n = int(input())
for _ in range(n):
    p = int(input())
    datas = [input().split() for _ in range(p)]
    print(solution(p, datas))
