import sys
from collections import deque

input = sys.stdin.readline

def solution(n, m, num):
    queue = deque(range(1, n + 1))
    answer = 0
    idx = 0
    while idx < m:
        if queue[0] == num[idx]:
            queue.popleft()
            idx += 1
            continue

        length = len(queue)
        st, end = 0, length - 1
        t = None
        for i in range(length):
            if queue[i] == num[idx]:
                t = i
                break

        l = abs(st - t)
        r = abs(end - t)
        if l <= r:
            for _ in range(l):
                answer += 1
                queue.append(queue.popleft())
        else:
            for _ in range(r + 1):
                answer += 1
                queue.appendleft(queue.pop())

    return answer

n, m = map(int, input().split())
num = list(map(int, input().split()))
print(solution(n, m, num))
