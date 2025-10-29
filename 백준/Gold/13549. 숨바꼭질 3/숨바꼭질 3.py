from collections import deque
import sys

input = sys.stdin.readline

def solution(n, k):
    time = [-1] * 100_001
    time[n] = 0
    queue = deque([n])
    if n == k:
        return 0
    while queue:
        curr = queue.popleft()
        if curr == k:
            return time[k]
        # for next in [curr - 1, curr + 1, curr * 2]:
        for next in [curr * 2, curr - 1, curr + 1]:
            if (0 <= next <= 100_000) and (time[next] == -1):
                if curr * 2 == next:
                    time[next] = time[curr]
                else:
                    time[next] = time[curr] + 1
                queue.append(next)

n, k = map(int, input().split())
print(solution(n, k))