import sys
import heapq

input = sys.stdin.readline

def solution(N, K, A, B):
    queue = []
    days = 1
    for _ in range(N):
        heapq.heappush(queue, K)
    while True:
        poped = [heapq.heappop(queue) + B for _ in range(A)]
        for value in poped:
            heapq.heappush(queue, value)
        for idx in range(N):
            queue[idx] -= 1
            if queue[idx] == 0:
                return days
        days += 1

N, K, A, B = map(int, input().split())
print(solution(N, K, A, B))

