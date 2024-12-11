drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(board):

    def backtracking(row, col):
        if len(lst) == 7:
            val = "".join(lst)
            if val not in check:
                check.add(val)
                nonlocal answer
                answer += 1
            return
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if 0 <= nrow < 4 and 0 <= ncol < 4:
                lst.append(board[nrow][ncol])
                backtracking(nrow, ncol)
                lst.pop()

    check = set()
    answer = 0
    lst = []

    for row in range(4):
        for col in range(4):
            backtracking(row, col)

    return answer

T = int(input())
for seq in range(T):
    board = [input().rstrip().split() for _ in range(4)]
    print(f'#{seq + 1} {solution(board)}')