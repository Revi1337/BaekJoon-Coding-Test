import heapq
import sys

input = sys.stdin.readline

"""
이번에는 그냥 heapq 를 사용. 이제 와전 이진트리를 이용한 최대힙을 직접 구현해보자.
"""

def solution(n, operations):
    numbers = []
    for operation in operations:
        if operation == 0:
            if not len(numbers):
                print(0)
            else:
                answer = heapq.heappop(numbers)[1]
                print(answer)
        else:
            heapq.heappush(numbers, (-operation, operation))

n = int(input().rstrip())
operations = [int(input().rstrip()) for _ in range(n)]
solution(n, operations)