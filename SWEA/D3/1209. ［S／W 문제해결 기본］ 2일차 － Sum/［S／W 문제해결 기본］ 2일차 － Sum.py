def solution(seq, board):
    answer = 0
    # 행
    for row in board:
        answer = max(answer, sum(row))
    # 열
    for col in range(100):
        answer = max(answer, sum([row[col] for row in board]))
    # 좌 대각선
    pre = 0
    for offset in range(100):
        pre += board[offset][offset]
    answer = max(answer, pre)
    # 우 대각선
    pre = 0
    for offset in range(100):
        pre += board[offset][100 - offset - 1]
    answer = max(answer, pre)
    return f'#{seq} {answer}'

T = 10
for _ in range(T):
    s = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    print(solution(s, board))