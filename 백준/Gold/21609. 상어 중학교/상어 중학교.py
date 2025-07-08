drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, board):

    EMPTY = -10
    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    def find_cluster():
        clusters, check = [], [[0] * N for _ in range(N)]
        for row in range(N):
            for col in range(N):
                if board[row][col] > 0 and not check[row][col]:
                    curr, stack, = board[row][col], [[row, col]]
                    cluster, zcheck = {0: 0, 'pos': [], 'stand': [1e9, 1e9]}, set()
                    check[row][col] = 1

                    while stack:
                        r, c = stack.pop()

                        cluster['pos'].append([r, c])
                        if board[r][c] == 0:
                            cluster[0] += 1
                        elif board[r][c] == curr:
                            if r <= cluster['stand'][0] and c <= cluster['stand'][1]:
                                cluster['stand'][0], cluster['stand'][1] = r, c

                        for d in range(4):
                            nr, nc = r + drow[d], c + dcol[d]
                            if not inside(nr, nc) or board[nr][nc] == -1:
                                continue
                            if board[nr][nc] == curr and not check[nr][nc]:
                                check[nr][nc] = 1
                                stack.append([nr, nc])
                            elif board[nr][nc] == 0 and (nr, nc) not in zcheck:
                                zcheck.add((nr, nc))
                                stack.append([nr, nc])

                    if len(cluster['pos']) >= 2:
                        clusters.append(cluster)

        clusters.sort(key = lambda clus: (-len(clus['pos']), -clus[0], -clus['stand'][0], -clus['stand'][1]))
        return clusters[0] if clusters else []

    def erase(poss):
        for row, col in poss:
            board[row][col] = EMPTY

    def gravity():
        for col in range(N):
            for row in range(N - 2, -1, -1):
                if board[row][col] != -1:
                    srow, scol = row, col
                    while True:
                        nrow, ncol = srow + drow[2], scol + dcol[2],
                        if not inside(nrow, ncol) or board[nrow][ncol] != EMPTY:
                            break
                        board[nrow][ncol], board[srow][scol] = board[srow][scol], board[nrow][ncol]
                        srow, scol = nrow, ncol

    def rotate():
        return [list(row) for row in zip(*board)][::-1]

    ans = 0
    while True:
        cluster = find_cluster()
        if not cluster:
            return ans

        ans, poss = ans + len(cluster['pos']) ** 2 , cluster['pos']
        erase(poss)
        gravity()
        board = rotate()
        gravity()


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))