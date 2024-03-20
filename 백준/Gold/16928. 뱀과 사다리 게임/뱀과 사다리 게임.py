from collections import deque
import sys

input = sys.stdin.readline

def solution(n, m, lathers, snakes):
    lathers = {lather[0]: lather[1] for lather in lathers}
    snakes = {snake[0]: snake[1] for snake in snakes}
    check = [-1] * 101
    check[1] = 0
    queue = deque([1])
    while queue:
        distance = queue.popleft()
        if distance == 100:
            return check[100]
        for number in range(6, 0, -1):
            next_distance = distance + number
            if 1 <= next_distance <= 100 and check[next_distance] == -1:
                if next_distance in lathers:
                    next_distance = lathers[next_distance]
                if next_distance in snakes:
                    next_distance = snakes[next_distance]
                if check[next_distance] == -1:
                    check[next_distance] = check[distance] + 1
                    queue.append(next_distance)

n, m = map(int, input().split())
lathers = [list(map(int, input().split())) for _ in range(n)]
snakes = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, lathers, snakes))