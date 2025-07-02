def solution(N, M, K, S):

    def rotate():
        rsize, csize = len(sti), len(sti[0])
        ssti = [[0] * rsize for _ in range(csize)]
        for row in range(rsize):
            for col in range(csize):
                ssti[col][rsize - 1 - row] = sti[row][col]
        return ssti

    def can_attach(brow, bcol):
        rsize, csize = len(sti), len(sti[0])
        if brow + rsize > N or bcol + csize > M:
            return False

        for row in range(rsize):
            for col in range(csize):
                if sti[row][col] == 1 and board[brow + row][bcol + col] == 1:
                    return False
        return True

    def attach(brow, bcol):
        rsize, csize = len(sti), len(sti[0])
        for row in range(rsize):
            for col in range(csize):
                if sti[row][col] == 1:
                    board[brow + row][bcol + col] = 1

    board = [[0] * M for _ in range(N)]
    for idx in range(K):
        sti = S[idx]
        attached = False
        for _ in range(4):
            for brow in range(N):
                for bcol in range(M):
                    if can_attach(brow, bcol):
                        attach(brow, bcol)
                        attached = True
                        break
                if attached:
                    break
            if attached:
                break
            sti = rotate()

    return sum(sum(line) for line in board)

N, M, K = map(int, input().split())
S = []
for _ in range(K):
    r, _ = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(r)]
    S.append(s)
print(solution(N, M, K, S))
