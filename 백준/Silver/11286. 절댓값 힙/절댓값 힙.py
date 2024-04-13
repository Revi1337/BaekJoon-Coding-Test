import heapq
import sys

input = sys.stdin.readline

def solution(operations):
    numbers = []
    for operation in operations:
        if operation != 0:
            heapq.heappush(numbers, (abs(operation), operation))
        else:
            if numbers:
                answer = heapq.heappop(numbers)[1]
                print(answer)
            else:
                print(0)

n = int(input().rstrip())
operations = [int(input().rstrip()) for _ in range(n)]
solution(operations)
