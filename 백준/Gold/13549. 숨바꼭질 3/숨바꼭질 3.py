from collections import deque

def solution(n, k):
    time = [-1] * 100_001
    time[n] = 0
    queue = deque([n])
    if n == k:
        return 0
    while queue:
        curr_distance = queue.popleft()
        if curr_distance == k:
            return time[k]
        for next_distance in [curr_distance * 2, curr_distance - 1, curr_distance + 1]:
            if (0 <= next_distance <= 100_000) and (time[next_distance] == -1):
                if curr_distance * 2 == next_distance:
                    time[next_distance] = time[curr_distance] + 0
                else:
                    time[next_distance] = time[curr_distance] + 1
                queue.append(next_distance)

n, k = map(int, input().split())
print(solution(n, k))
