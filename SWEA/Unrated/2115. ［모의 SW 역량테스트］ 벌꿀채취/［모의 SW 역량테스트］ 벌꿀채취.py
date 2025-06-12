def solution(N, M, C, board):

    def backtrack(n, amount, sm, sr, sc):
        nonlocal mx
        if amount > C:
            return
        if n == M:
            mx = max(mx, sm)
            return

        backtrack(n + 1, amount + board[sr][sc + n], sm + board[sr][sc + n] ** 2, sr, sc)
        backtrack(n + 1, amount, sm, sr, sc)

    answer = 0
    for row1 in range(N):
        for col1 in range(N - M + 1):
            mx = 0
            backtrack(0, 0, 0, row1, col1)
            first = mx
            for row2 in range(row1, N):
                c2 = col1 + M if row1 == row2 else 0
                for col2 in range(c2, N - M + 1):
                    mx = 0
                    backtrack(0, 0, 0, row2, col2)
                    answer = max(answer, first + mx)

    return answer

T = int(input())
for seq in range(T):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{seq + 1} {solution(N, M, C, board)}')
