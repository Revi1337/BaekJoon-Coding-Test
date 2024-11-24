def solution(N, board):
    new_board = [[[0] * N for _ in range(N)] for _ in range(3)]
    for row in range(N):
        for col in range(N):
            new_board[0][col][N - 1 - row] = board[row][col]
            new_board[1][N - 1 - row][N - 1 - col] = board[row][col]
            new_board[2][N - 1 - col][row] = board[row][col]

    answer = list(zip(*new_board))
    for ans in answer:
        for line in ans:
            print("".join(map(str, line)), end = ' ')
        print()

T = int(input())
for seq in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{seq + 1}')
    solution(N, board)
