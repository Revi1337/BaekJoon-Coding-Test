def solution(N, M, board):
    dp = [[0] * (M + 2) for _ in range(N + 2)]
    for row in range(1, N + 1):
        for col in range(1, M + 1):
            dp[row][col] = board[row][col] + max(dp[row - 1][col - 1], dp[row][col - 1], dp[row - 1][col])

    return dp[N][M]

N, M = map(int, input().rstrip().split())
board = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
board.insert(0, [0] * (M + 2))
board.append([0] * (M + 2))
print(solution(N, M, board))
