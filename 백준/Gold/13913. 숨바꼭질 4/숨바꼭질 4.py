from collections import deque
import sys

input = sys.stdin.readline

def solution(n, k):
    queue = deque()
    queue.append(n)
    check = [0] * 100_001
    tracking = [0] * 100_001
    while queue:
        distance = queue.popleft()
        if distance == k:
            print(check[distance])
            data = []
            tmp = distance
            for _ in range(check[distance] + 1):
                data.append(tmp)
                tmp = tracking[tmp]
            print(" ".join(map(str, data[::-1])))
            return
        for next_distance in (distance - 1, distance + 1, distance * 2):
            if (0 <= next_distance <= 100_000) and check[next_distance] == 0:
                check[next_distance] = check[distance] + 1
                queue.append(next_distance)
                tracking[next_distance] = distance

n, k = map(int, input().split())
solution(n, k)