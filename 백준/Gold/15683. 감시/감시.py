drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def one(d, sr, sc, board):
    """ 하나의 방향으로 감시한다. """
    n_board = [[*line] for line in board]
    r, c = sr, sc
    while True:
        nr, nc = r + drow[d], c + dcol[d]
        if not (0 <= nr < N and 0 <= nc < M) or (n_board[nr][nc] == '6'):
            break
        if n_board[nr][nc] == '0':
            n_board[nr][nc] = '#'
        r, c = nr, nc
    return n_board


def two(d, sr, sc, board):
    """ 양쪽 방향으로 감시한다. """
    n_board = [[*line] for line in board]
    if d in [0, 2]:
        direction = (-1, 0), (1, 0)
    else:
        direction = (0, -1), (0, 1)
    for drow, dcol in direction:
        r, c = sr, sc
        while True:
            nr, nc = r + drow, c + dcol
            if not (0 <= nr < N and 0 <= nc < M) or (n_board[nr][nc] == '6'):
                break
            if n_board[nr][nc] == '0':
                n_board[nr][nc] = '#'
            r, c = nr, nc
    return n_board


def three(d, sr, sc, board):
    """ 90도 방향으로 검사한다. """
    n_board = [[*line] for line in board]
    direction = None
    if d == 0:
        direction = (-1, 0), (0, 1)
    elif d == 1:
        direction = (0, 1), (1, 0)
    elif d == 2:
        direction = (1, 0), (0, -1)
    elif d == 3:
        direction = (0, -1), (-1, 0)

    for drow, dcol in direction:
        r, c = sr, sc
        while True:
            nr, nc = r + drow, c + dcol
            if not (0 <= nr < N and 0 <= nc < M) or (n_board[nr][nc] == '6'):
                break
            if n_board[nr][nc] == '0':
                n_board[nr][nc] = '#'
            r, c = nr, nc
    return n_board

def four(d, sr, sc, board):
    """ 세개의 방향을 검사한다. """
    n_board = [[*line] for line in board]
    direction = None
    if d == 0:
        direction = (-1, 0), (0, -1), (0, 1)
    elif d == 1:
        direction = (-1, 0), (0, 1), (1, 0)
    elif d == 2:
        direction = (0, 1), (1, 0), (0, -1)
    elif d == 3:
        direction = (0, -1), (-1, 0), (1, 0)

    for drow, dcol in direction:
        r, c = sr, sc
        while True:
            nr, nc = r + drow, c + dcol
            if not (0 <= nr < N and 0 <= nc < M) or (n_board[nr][nc] == '6'):
                break
            if n_board[nr][nc] == '0':
                n_board[nr][nc] = '#'
            r, c = nr, nc
    return n_board


def five(d, sr, sc, board):
    """ 모든 방향을 감시한다. """
    n_board = [[*line] for line in board]
    for drow, dcol in (-1, 0), (0, 1), (1, 0), (0, -1):
        r, c = sr, sc
        while True:
            nr, nc = r + drow, c + dcol
            if not (0 <= nr < N and 0 <= nc < M) or (n_board[nr][nc] == '6'):
                break
            if n_board[nr][nc] == '0':
                n_board[nr][nc] = '#'
            r, c = nr, nc
    return n_board

def solution(N, M, board):

    def backtracking(n, board):
        if n == cctv_length:
            cnt = 0
            for row in range(N):
                for col in range(M):
                    if board[row][col] == '0':
                        cnt += 1
            nonlocal answer
            answer = min(answer, cnt)
            return

        cr, cc = cctv[n]
        rotate = callable[board[cr][cc]]

        backtracking(n + 1, rotate(0, cr, cc, board)) # 기본
        backtracking(n + 1, rotate(1, cr, cc, board)) # 90 도
        backtracking(n + 1, rotate(2, cr, cc, board)) # 180 도
        backtracking(n + 1, rotate(3, cr, cc, board)) # 270 도

    callable = {
        '1': one,
        '2': two,
        '3': three,
        '4': four,
        '5': five
    }

    cctv, cctv_length = [], 0
    for row in range(N):
        for col in range(M):
            if board[row][col] != '0' and board[row][col] != '6':
                cctv_length += 1
                cctv.append((row, col))

    answer = 1e9
    backtracking(0, board)

    return answer

N, M = map(int, input().split())
board = [list(input().rstrip().split()) for _ in range(N)]
print(solution(N, M, board))