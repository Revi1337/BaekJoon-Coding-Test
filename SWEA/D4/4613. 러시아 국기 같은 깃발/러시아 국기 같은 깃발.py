def solution(N, M, board):
    answer = 2500
    for b in range(1, N - 1):
        for r in range(b + 1, N):
            counter = 0
            white, blue, red = board[:b], board[b:r], board[r:]
            for row in white:
                counter += M - row.count('W')
            for row in blue:
                counter += M - row.count('B')
            for row in red:
                counter += M - row.count('R')

            answer = min(answer, counter)

    return answer

T = int(input())
for seq in range(T):
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    print(f'#{seq + 1} {solution(N, M, board)}')