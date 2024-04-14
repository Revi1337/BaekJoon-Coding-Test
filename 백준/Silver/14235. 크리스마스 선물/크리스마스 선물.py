import sys
import heapq

input = sys.stdin.readline

def solution(n, lst):
    queue = []
    for numbers in lst:
        if numbers[0] == 0:
            if not queue:
                print(-1)
            else:
                print(-(heapq.heappop(queue)))
        else:
            for number in numbers[1:]:
                heapq.heappush(queue, -number)

n = int(input().rstrip())
lst = [list(map(int, input().split())) for _ in range(n)]
solution(n, lst)



