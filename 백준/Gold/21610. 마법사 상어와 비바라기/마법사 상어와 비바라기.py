drow = [0, -1, -1, -1, 0, 1, 1, 1]
dcol = [-1, -1, 0, 1, 1, 1, 0, -1]

def solution(N, M, board, operations):
    cloud = {(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)}
    for dir, depth in operations:
        dir -= 1
        tcloud = set()
        for row, col in cloud:
            nrow = (row + drow[dir] * depth) % N
            ncol = (col + dcol[dir] * depth) % N
            board[nrow][ncol] += 1
            tcloud.add((nrow, ncol))

        for row, col in tcloud:
            cnt = 0
            for d in [1,3,5,7]:
                nrow, ncol = row + drow[d], col + dcol[d]
                if 0 <= nrow < N and 0 <= ncol < N and board[nrow][ncol] > 0:
                    cnt += 1
            board[row][col] += cnt

        ncloud = set()
        for row in range(N):
            for col in range(N):
                if board[row][col] >= 2 and (row, col) not in tcloud:
                    board[row][col] -= 2
                    ncloud.add((row, col))

        cloud = ncloud

    return sum(sum(line) for line in board)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
operations = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, board, operations))
