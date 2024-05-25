import sys

open = sys.stdin.readline

def solution(N, position):
    distance = [0]
    for idx in range(1, N):
        dist = abs(position[idx - 1][0] - position[idx][0]) + abs(position[idx - 1][1] - position[idx][1])
        distance.append(dist)

    total = sum(distance)
    answer = 1e9
    for i in range(1, N - 1):
        # distance 의 합에서 distance 배열의 현재 idx 양옆 (idx - 1, idx + 1) 을 빼주고,
        # 원본 배열의 현재 idx 양옆 (idx - 1, idx + 1) 의 거리를 다시 더해준다
        dist = total \
               - (distance[i] + distance[i + 1]) \
               + abs(position[i + 1][0] - position[i - 1][0]) \
               + abs(position[i + 1][1] - position[i - 1][1])
        answer = min(answer, dist)
    return answer

N = int(input())
position = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, position))
