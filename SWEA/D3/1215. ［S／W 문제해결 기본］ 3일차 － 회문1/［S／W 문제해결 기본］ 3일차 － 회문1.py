def solution(seq, N, board):
    answer = 0
    length = 8
    for row in board:
        for col in range(length - N + 1):
            if row[col: col + N] == row[col: col + N][::-1]:
                answer += 1
    for col in range(8):
        string = "".join([row[col] for row in board])
        for idx in range(length - N + 1):
            if string[idx: idx + N] == string[idx: idx + N][::-1]:
                answer += 1

    return f'#{seq} {answer}'

T = 10
for idx in range(T):
    N = int(input())
    board = [input().rstrip() for _ in range(8)]
    print(solution(idx + 1, N, board))