import sys
import heapq

input = sys.stdin.readline

def solution(N, K, J, B):
    J.sort()
    B.sort()

    res = jpoint = 0
    mheap = []
    for bag in B:
        while jpoint < N and J[jpoint][0] <= bag:
            heapq.heappush(mheap, -J[jpoint][1])
            jpoint += 1
        if mheap:
            res += -heapq.heappop(mheap)

    return res

N, K = map(int, input().split())
J = [list(map(int, input().split())) for _ in range(N)]
B = [int(input()) for _ in range(K)]
print(solution(N, K, J, B))