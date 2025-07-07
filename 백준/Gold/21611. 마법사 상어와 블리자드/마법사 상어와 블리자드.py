# 상 하 좌 우
mrow = [-1, 1, 0, 0]
mcol = [0, 0, -1, 1]

# 우 하 좌 상
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

def solution(N, M, board, opers):
    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    mid = N // 2
    d, check, line = 0, [[0] * N for _ in range(N)], [[0, 0, board[0][0]]]
    check[0][0], row, col = 1, 0, 0

    while row != mid or col != mid:
        nrow, ncol = row + drow[d], col + dcol[d]
        if not inside(nrow, ncol) or check[nrow][ncol]:
            d = (d + 1) % 4
        else:
            check[nrow][ncol] = 1
            line.append([nrow, ncol, board[nrow][ncol]])
            row, col = nrow, ncol
    line[-1][2] = -1
    line = line[::-1]

    pidx = {(r, c): i for i, (r, c, _) in enumerate(line)}

    ans = [0] * 4
    for d, s in opers:
        d -= 1
        for dist in range(1, s + 1):
            r, c = mid + mrow[d] * dist, mid + mcol[d] * dist
            idx = pidx.get((r, c))
            if idx is not None:
                line[idx][2] = 0

        balls = [x[2] for x in line if x[2] > 0]

        while True:
            nballs = []
            changed = False
            idx = 0
            while idx < len(balls):
                jdx = idx
                while jdx < len(balls) and balls[idx] == balls[jdx]:
                    jdx += 1
                if jdx - idx >= 4:
                    ans[balls[idx]] += (jdx - idx)
                    changed = True
                else:
                    nballs.extend(balls[idx:jdx])
                idx = jdx
            if not changed:
                break
            balls = nballs

        transformed = []
        idx = 0
        while idx < len(balls):
            jdx = idx
            while jdx < len(balls) and balls[idx] == balls[jdx]:
                jdx += 1
            transformed.extend([jdx - idx, balls[idx]])
            idx = jdx

        for idx in range(1, len(line)):
            if idx - 1 < len(transformed):
                line[idx][2] = transformed[idx - 1]
            else:
                line[idx][2] = 0

    return ans[1] * 1 + ans[2] * 2 + ans[3] * 3


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
opers = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, board, opers))
