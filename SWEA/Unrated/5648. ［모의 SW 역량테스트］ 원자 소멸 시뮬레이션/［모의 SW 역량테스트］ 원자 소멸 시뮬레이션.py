# 상 하 좌 우
DROW = [1, -1, 0, 0]
DCOL = [0, 0, -1, 1]

def solution(N, arr):
    d = [0] * N
    am = [0] * N

    for idx in range(N):
        x, y, dir, energy = arr[idx]
        x = (x + 1000) * 2
        y = (y + 1000) * 2
        arr[idx][0], arr[idx][1] = y, x
        d[idx] = dir
        am[idx] = energy

    answer = 0
    active = [True] * N

    for _ in range(4001):
        pos_map = {}

        for i in range(N):
            if not active[i]:
                continue
            nr = arr[i][0] + DROW[d[i]]
            nc = arr[i][1] + DCOL[d[i]]
            if not (0 <= nr <= 4000 and 0 <= nc <= 4000):
                active[i] = False
                continue
            arr[i][0], arr[i][1] = nr, nc
            if (nr, nc) not in pos_map:
                pos_map[(nr, nc)] = []
            pos_map[(nr, nc)].append(i)

        for atoms in pos_map.values():
            if len(atoms) >= 2:
                for i in atoms:
                    if active[i]:
                        answer += am[i]
                        active[i] = False

        if not any(active):
            break

    return answer

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{t} {solution(N, arr)}")