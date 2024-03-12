import sys

input = sys.stdin.readline

def solution(t, entries):
    max_floor = max_room = -float('inf')
    for floor, room in entries:
        if max_floor < floor:
            max_floor = floor
        if max_room < room:
            max_room = room

    dp_table = [[0] * (max_room + 1) for _ in range(max_floor + 1)]
    for room in range(1, max_room + 1):
        dp_table[0][room] = room

    for floor in range(1, max_floor + 1):
        for room in range(1, max_room + 1):
            dp_table[floor][room] = sum(dp_table[floor - 1][1 : room + 1])

    for floor, room in entries:
        print(dp_table[floor][room])

t = int(input().rstrip())
entries = [[int(input().rstrip()), int(input().rstrip())] for _ in range(t)]
solution(t, entries)