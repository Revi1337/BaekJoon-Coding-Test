def solution(N, board):

    def backtracking(n, ml):
        nonlocal answer
        if answer >= ml:
            return
        if n == N:
            answer = max(answer, ml)
            return
        for chore in range(N):
            if not check[chore]:
                check[chore] = 1
                backtracking(n + 1, ml * (board[n][chore] / 100))
                check[chore] = 0

    answer = 0
    check = [0] * N
    backtracking(0, 100)

    return answer

T = int(input())
for seq in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{seq + 1} {solution(N, board):.6f}')