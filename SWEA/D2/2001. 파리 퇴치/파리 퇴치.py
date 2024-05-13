def solution(idx, N, M, board):
    maxN = 0
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            total = 0
            for tmp in range(row, row + M):
                total += sum(board[tmp][col: col + M])
            if total > maxN:
                maxN = total
    return f'#{idx} {maxN}'

T = int(input().rstrip())
for idx in range(T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(solution(idx + 1, N, M, board))
