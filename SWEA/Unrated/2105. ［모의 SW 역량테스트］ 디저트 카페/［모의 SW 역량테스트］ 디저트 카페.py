drow = [1, 1, -1, -1, 1]
dcol = [-1, 1, 1, -1, -1]

def solution(N, board):

    def backtracking(d, r, c, lst):
        nonlocal answer
        if d == 2 and len(lst) * 2 <= answer:
            return
        if d > 3:
            return
        if d == 3 and (r, c) == (row, col):
            answer = max(answer, len(lst))
            return
        for nd in range(d, d + 2):
            nr, nc = r + drow[nd], c + dcol[nd]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] not in lst:
                lst.append(board[nr][nc])
                backtracking(nd, nr, nc, lst)
                lst.pop()

    answer = -1
    for row in range(N - 2):
        for col in range(N - 1):
            backtracking(0, row, col, [])

    return answer

T = int(input())
for seq in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{seq + 1} {solution(N, board)}')
