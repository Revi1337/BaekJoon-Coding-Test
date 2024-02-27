from collections import deque

def solution(n, k):
    distance = [0] * 100_001
    queue = deque([n])
    while queue:
        curr_distance = queue.popleft()
        if curr_distance == k:
            return distance[k]
        for next_distance in [curr_distance - 1, curr_distance + 1, curr_distance * 2]:
            if 0 <= next_distance <= 100_000 and not distance[next_distance]:
                distance[next_distance] = distance[curr_distance] + 1
                queue.append(next_distance)

n, k = map(int, input().split())
print(solution(n, k))