def solution(N, board):

    def backtracking(n, cnt):
        nonlocal answer
        if cnt + digon_length - n <= answer:
            return

        if n == digon_length:
            answer = max(answer, cnt)
            return

        for row, col in digon[n]:
            if check[row - col] == 0:
                check[row - col] = 1
                backtracking(n + 1, cnt + 1)
                check[row - col] = 0
        backtracking(n + 1, cnt)

    check = [0] * (2 * N)
    digon, digon_length = [[] for _ in range(2 * N - 1)], 2 * N - 1
    total_cnt = 0
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                total_cnt += 1
                digon[row + col].append((row, col))

    answer = 0
    backtracking(0, 0)

    return answer

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))
