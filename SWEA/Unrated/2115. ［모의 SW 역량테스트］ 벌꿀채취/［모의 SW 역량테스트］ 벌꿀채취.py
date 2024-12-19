def solution(N, M, C, board):

    def backtracking(n, cnt, sm, ci, cj):
        nonlocal mx
        if cnt > C:
            return
        if n == M:
            mx = max(mx, sm)
            return

        backtracking(n + 1, cnt + board[ci][cj + n], sm + board[ci][cj + n] ** 2, ci, cj)
        backtracking(n + 1, cnt, sm, ci, cj)

    ans = mx = sm1 = 0
    memo = [[0] * N for _ in range(N)]
    # [0] 각 위치의 가능한 최대값을 한번 저장.
    for i in range(N):
        for j in range(N - M + 1):
            mx = 0
            backtracking(0, 0, 0, i, j)
            memo[i][j] = mx

    # [1] 가능한 모든 시작위치 (일꾼 1, 2)
    for i1 in range(N): # 첫번쨰 일꾼
        for j1 in range(N - M + 1):
            for i2 in range(i1, N): # 두번쨰 일꾼 (가능한 모든 2명의 일꾼 위치)
                sj = j1 + M if i1 == i2 else 0
                for j2 in range(sj, N - M + 1):
                    ans = max(ans, memo[i1][j1] + memo[i2][j2])

    return ans

T = int(input())
for seq in range(T):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{seq + 1} {solution(N, M, C, board)}')