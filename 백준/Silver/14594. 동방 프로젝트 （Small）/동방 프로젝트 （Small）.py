import sys

input = sys.stdin.readline

def solution(N, M, jong):
    rooms = [0] * (N + 1)
    for x, y in jong:
        for room in range(x, y):
            rooms[room] = 1

    return rooms.count(0) - 1

N = int(input())
M = int(input())
jong = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, jong))
