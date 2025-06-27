def solution(N, board):
    dp = [[0] * (N + 1) for _ in range(2)]
    dp[0][1], dp[1][1] = board[0][0], board[1][0]

    for idx in range(2, N + 1):
        dp[0][idx] = max(dp[1][idx - 1], dp[0][idx - 2], dp[1][idx - 2]) + board[0][idx - 1]
        dp[1][idx] = max(dp[0][idx - 1], dp[0][idx - 2], dp[1][idx - 2]) + board[1][idx - 1]

    return max(dp[0][-1], dp[1][-1])

T = int(input())
for _ in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]
    print(solution(N, board))
