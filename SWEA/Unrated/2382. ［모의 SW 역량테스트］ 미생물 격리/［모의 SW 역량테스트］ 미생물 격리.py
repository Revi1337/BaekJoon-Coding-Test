drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]
dmap = {0: 1, 1: 0, 2: 3, 3: 2}

def solution(N, M, K, entries):
    for lst in entries:
        lst[3] -= 1

    edges = set()
    for row in range(N):
        for col in range(N):
            if row == 0 or row == N - 1 or col == 0 or col == N - 1:
                edges.add((row, col))

    while M > 0:
        nxt = {}
        for r, c, cnt, d in entries:
            nrow, ncol = r + drow[d],  c + dcol[d]
            if (nrow, ncol) in edges:
                cnt //= 2
                d = dmap[d]
            nxt[(nrow, ncol)] = nxt.get((nrow, ncol), [])
            nxt[(nrow, ncol)].append((nrow, ncol, cnt, d))

        entries = []
        for pos in nxt:
            if len(nxt[pos]) > 1:
                sm = sum(entry[2] for entry in nxt[pos])
                mx = max(nxt[pos], key = lambda x: x[2])
                d = mx[3]
                entries.append([mx[0], mx[1], sm, d])
            else:
                entries.append([*nxt[pos][0]])
        M -= 1

    return sum(entry[2] for entry in entries)

T = int(input())
for seq in range(T):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(K)]
    print(f'#{seq + 1} {solution(N, M, K, board)}')