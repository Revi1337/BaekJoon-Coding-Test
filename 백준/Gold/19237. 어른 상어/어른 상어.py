# 상 하 좌 우
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def solution(N, M, K, board, sdirs, pri):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    for col in range(M):
        sdirs[col] -= 1
    for s in range(M):
        for row in range(4):
            for col in range(4):
                pri[s][row][col] -= 1

    sharks = [None for _ in range(M)]
    nboard = [[None for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if board[row][col]:
                board[row][col] -= 1
                sharks[board[row][col]] = [row, col]
                nboard[row][col] = [board[row][col], K]
    board = nboard

    ans = 0
    while True:
        ndirs, npos = [None] * M, {},                               # 다음 방향, 다음 좌표들
        for shark in range(M):
            if sharks[shark] is None:
                continue
            srow, scol = sharks[shark]
            sdir = sdirs[shark]

            for d in pri[shark][sdir]:                              # 먼저 가능한(냄새가 있지 않은) 좌표를 찾는다. (우선순위대로)
                nrow, ncol = srow + drow[d], scol + dcol[d]
                if inside(nrow, ncol):
                    if board[nrow][ncol] is None:
                        pos = (nrow, ncol)
                        npos[pos] = npos.get(pos, [])
                        npos[pos].append(shark)
                        ndirs[shark] = d
                        break
            else:                                                   # 가능한(냄새가 있지 않은) 좌표가 없다면, 이미 있는 냄새들 중 자신의 냄새 좌표의 위치로 바꾼다.
                for d in pri[shark][sdir]:
                    nrow, ncol = srow + drow[d], scol + dcol[d]
                    if inside(nrow, ncol):
                        if board[nrow][ncol][0] == shark:
                            pos = (nrow, ncol)
                            npos[pos] = npos.get(pos, [])
                            npos[pos].append(shark)
                            ndirs[shark] = d
                            break

        for row in range(N):                                    # 냄새들을 1씩 지운다.
            for col in range(N):
                if board[row][col] is not None:
                    board[row][col][1] -= 1
                    if board[row][col][1] == 0:
                        board[row][col] = None

        nsharks = [None] * M
        for key, shs in npos.items():
            shs.sort()                                          # 겹치는 좌표들을 상어 번호 순으로 정렬
            nrow, ncol = key
            sh = shs[0]
            board[nrow][ncol] = [sh, K]
            nsharks[sh] = [nrow, ncol]                          # 다음 상어 좌표들을 일단 취합

        sharks, sdirs = nsharks, ndirs
        ans += 1

        left = False
        for s in sharks[1:]:
            if s is not None:
                left = True
                break
        if sharks[0] is not None and not left:
            return ans
        if ans >= 1000:
            return -1

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = list(map(int, input().split()))
pri = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
print(solution(N, M, K, board, dirs, pri))