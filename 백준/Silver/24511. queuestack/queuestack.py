import sys
from collections import deque

input = sys.stdin.readline

'''
queuestack (https://www.acmicpc.net/problem/24511)
- 시간이 상당히 오래걸림. Queue 는 항상 맨뒤에서 pop 하므로, 무시할 수 있음
- A[idx] 가 1 (Queue) 인 자료구조만 하나로 이어서 생각한다.
2024-08-13
'''

def solution(N, A, B, M, C):
    queue = deque([])
    for idx in range(N):
        if not A[idx]:
            queue.appendleft(B[idx])
    if not queue:
        print(*C, sep = ' ')
        return
    for idx in range(M):
        queue.append(C[idx])
        print(queue.popleft(), end = ' ')


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
solution(N, A, B, M, C)