from collections import deque

def solution(integer):
    queue = deque(range(1, integer + 1))
    while len(queue) != 1:
        queue.popleft()
        queue.rotate(-1)
    return queue.popleft()

integer = int(input())
print(solution(integer))
