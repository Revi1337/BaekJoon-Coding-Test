import sys

input = sys.stdin.readline

def solution(p, m, players):
    rooms = [[[players[0][0], players[0][1]]]]
    for level, nickname in players[1:]:
        new = False
        for room in rooms:
            if (room[0][0] - 10) <= level <= (room[0][0] + 10):
                if len(room) < m:
                    room.append([level, nickname])
                    new = True
                    break
        if not new:
            rooms.append([[level, nickname]])

    for room in rooms:
        room.sort(key = lambda x: x[1])
        if len(room) == m:
            print('Started!')
        else:
            print('Waiting!')
        for l, n in room:
            print(f'{l} {n}')


p, m = map(int, input().split())
players = []
for _ in range(p):
    data = input().split()
    players.append([int(data[0]), data[1]])
solution(p, m, players)
