import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, board):

    EMPTY, ROCK, TEACH, STU = 'X', 'O', 'T', 'S'

    def check_left(srow, scol):
        for ncol in range(scol - 1, -1, -1):
            if board[srow][ncol] == ROCK:
                break
            if board[srow][ncol] == TEACH:
                return False
        return True

    def check_right(srow, scol):
        for ncol in range(scol + 1, N):
            if board[srow][ncol] == ROCK:
                break
            if board[srow][ncol] == TEACH:
                return False
        return True

    def check_up(srow, scol):
        for nrow in range(srow - 1, -1, -1):
            if board[nrow][scol] == ROCK:
                break
            if board[nrow][scol] == TEACH:
                return False
        return True

    def check_down(srow, scol):
        for nrow in range(srow + 1, N):
            if board[nrow][scol] == ROCK:
                break
            if board[nrow][scol] == TEACH:
                return False
        return True

    def possible(srow, scol):
        for callable in check_left, check_right, check_up, check_down:
            if not callable(srow, scol):
                return False
        return True

    def backtrack(n, check):
        nonlocal ans
        if ans:
            return
        if n == 3:
            for row, col in studs:
                if not possible(row, col):
                    break
            else:
                ans = 1
            return
        for idx in range(len(poss)):
            if not check[idx]:
                check[idx], board[poss[idx][0]][poss[idx][1]] = 1, ROCK
                backtrack(n + 1, check)
                check[idx], board[poss[idx][0]][poss[idx][1]] = 0, EMPTY

    poss, studs = [[] for _ in range(2)]
    for row in range(N):
        for col in range(N):
            if board[row][col] == EMPTY:
                poss.append([row, col])
            elif board[row][col] == STU:
                studs.append([row, col])

    ans = 0
    backtrack(0, [0] * len(poss))

    return 'YES' if ans else 'NO'

N = int(input())
board = [input().rstrip().split() for _ in range(N)]
print(solution(N, board))
