import sys
from collections import deque

input = sys.stdin.readline

def solution(n, m, priority):
    counter = 1
    queue = deque([*enumerate(priority)])
    while queue:
        index, priority = queue.popleft()
        hight_priority = priority
        for post_index, post_priority in queue:
            if post_priority > hight_priority:
                hight_priority = post_priority
        if hight_priority != priority:
            queue.append([index, priority])
            continue
        if index == m:
            return counter
        counter += 1

loop = int(input().rstrip())
for _ in range(loop):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    print(solution(n, m, priority))
