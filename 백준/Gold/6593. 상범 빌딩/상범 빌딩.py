from collections import deque

# 동 서 남 북 상 하
dheight = [0, 0, 0, 0, -1, 1]
drow = [0, 0, 1, -1, 0, 0]
dcol = [1, -1, 0, 0, 0, 0]

def solution(L, R, C, building):
    prolog = epilog = None
    for height in range(L):
        for row in range(R):
            for col in range(C):
                if building[height][row][col] == 'S':
                    prolog = (height, row, col)
                if building[height][row][col] == 'E':
                    epilog = (height, row, col)
                if (prolog is not None) and (epilog is not None):
                    break

    inside = lambda h, r, c : 0 <= h < L and 0 <= r < R and 0 <= c < C

    distance = [[[0] * C for _ in range(R)] for _ in range(L)]
    distance[prolog[0]][prolog[1]][prolog[2]] = 1
    queue = deque([tuple(prolog)])

    while queue:
        h, r, c = queue.popleft()
        if (h, r, c) == epilog:
            return f'Escaped in {distance[h][r][c] - 1} minute(s).'
        for d in range(6):
            nh, nr, nc = h + dheight[d], r + drow[d], c + dcol[d]
            if inside(nh, nr, nc) and building[nh][nr][nc] != '#' and not distance[nh][nr][nc]:
                distance[nh][nr][nc] = distance[h][r][c] + 1
                queue.append((nh, nr, nc))

    return 'Trapped!'


while True:
    string = input().rstrip()
    if string == '0 0 0':
        break
    L, R, C = map(int, string.split())
    building = []
    for _ in range(L):
        floor = [list(input().rstrip()) for _ in range(R)]
        _ = input()
        building.append(floor)

    print(solution(L, R, C, building))
