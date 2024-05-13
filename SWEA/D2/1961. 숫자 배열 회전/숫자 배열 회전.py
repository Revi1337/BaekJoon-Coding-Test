def solution(idx, N, board):
    answer1 = [[0] * N for _ in range(N)]
    answer2 = [[0] * N for _ in range(N)]
    answer3 = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            answer1[col][N - 1 - row] = board[row][col] # 90
            answer2[N - 1 - row][N - 1 - col] = board[row][col] # 180
            answer3[N - 1 - col][row] = board[row][col] # 270

    print(f'#{idx}')
    for row in range(N):
        print("".join(map(str, answer1[row])), end = ' ')
        print("".join(map(str, answer2[row])), end = ' ')
        print("".join(map(str, answer3[row])))

T = int(input())
for idx in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    solution(idx + 1, N, board)