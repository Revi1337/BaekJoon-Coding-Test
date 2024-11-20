def solution(board):
    answer = 0
    for line in board:
        answer = max(answer, sum(line))
    for col in range(100):
        answer = max(answer, sum([line[col] for line in board]))
    answer = max(answer, sum([board[idx][idx] for idx in range(100)]))
    answer = max(answer, sum([board[idx][99 - idx] for idx in range(100)]))

    return answer

T = 10
for _ in range(T):
    seq = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{seq} {solution(board)}')