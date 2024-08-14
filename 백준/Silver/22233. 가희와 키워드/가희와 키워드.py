import sys

input = sys.stdin.readline

'''
기획과 키워드 (https://www.acmicpc.net/problem/22233)
'''

def solution(N, M, memos, blogs):
    memos = set(memos)
    length = len(memos)
    for blog in blogs:
        for key in blog:
            if key in memos:
                memos.discard(key)
                length -= 1
        print(length)

N, M = map(int, input().split())
memos = [input().rstrip() for _ in range(N)]
blogs = [input().rstrip().split(',') for _ in range(M)]
solution(N, M, memos, blogs)
