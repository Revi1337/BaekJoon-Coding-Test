dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

def solution(N, M, x, y, K, board, opers):
    n1 = n2 = n3 = n4 = n5 = n6 = 0
    for operation in opers:
        nr, nc = x + dr[operation], y + dc[operation]
        if not (0 <= nr < N and 0 <= nc < M):
            continue

        if operation == 1:
            n1, n3, n4, n6 = n4, n1, n6, n3
        elif operation == 2:
            n1, n3, n4, n6 = n3, n6, n1, n4
        elif operation == 3:
            n1, n2, n5, n6 = n5, n1, n6, n2
        else:
            n1, n2, n5, n6 = n2, n6, n1, n5

        if board[nr][nc] == 0:
            board[nr][nc] = n6
        else:
            n6, board[nr][nc] = board[nr][nc], 0

        print(n1)
        x, y = nr, nc

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
opers = list(map(int, input().split()))
solution(N, M, x, y, K, board, opers)
