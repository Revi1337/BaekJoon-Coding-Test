from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def move(x, y, dx, dy, board):
    count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def solution(N, M, board):
    rr, rc, br, bc = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rr, rc = i, j
            elif board[i][j] == 'B':
                br, bc = i, j

    queue = deque([(rr, rc, br, bc, 0)])
    visited = set()
    visited.add((rr, rc, br, bc))

    while queue:
        rr, rc, br, bc, depth = queue.popleft()
        if depth >= 10:
            return -1

        for i in range(4):
            nrr, nrc, rcnt = move(rr, rc, drow[i], dcol[i], board)
            nbr, nbc, bcnt = move(br, bc, drow[i], dcol[i], board)

            if board[nbr][nbc] == 'O':
                continue
            if board[nrr][nrc] == 'O':
                return depth + 1
            if nrr == nbr and nrc == nbc:
                if rcnt > bcnt:
                    nrr -= drow[i]
                    nrc -= dcol[i]
                else:
                    nbr -= drow[i]
                    nbc -= dcol[i]

            if (nrr, nrc, nbr, nbc) not in visited:
                visited.add((nrr, nrc, nbr, nbc))
                queue.append((nrr, nrc, nbr, nbc, depth + 1))

    return -1

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
print(solution(N, M, board))