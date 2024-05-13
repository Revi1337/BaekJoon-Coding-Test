def solution(idx, board):
    for row in range(9):
        tmp = set(board[row])
        if len(tmp) != 9:
            return f'#{idx} 0'
    for col in range(9):
        tmp = set([line[col] for line in board])
        if len(tmp) != 9:
            return f'#{idx} 0'
    for row in range(0, 7, 3):
        for col in range(0, 7, 3):
            total = set()
            for tmp in range(row, row + 3):
                total.update(board[tmp][col: col + 3])
            if len(total) != 9:
                return f'#{idx} 0'
            
    return f'#{idx} 1'

T = int(input())
for idx in range(T):
    board = [list(map(int, input().split())) for _ in range(9)]
    print(solution(idx + 1, board))