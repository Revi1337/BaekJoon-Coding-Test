drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(board):

    def backtracking(n, num, row, col):
        if n == 7:
            answer.add(num)
            return
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if 0 <= nrow < 4 and 0 <= ncol < 4:
                backtracking(n + 1, num * 10 + board[nrow][ncol], nrow, ncol)

    answer = set()
    for row in range(4):
        for col in range(4):
            backtracking(0, 0, row, col)

    return len(answer)

T = int(input())
for seq in range(T):
    board = [list(map(int, input().split())) for _ in range(4)]
    print(f'#{seq + 1} {solution(board)}')