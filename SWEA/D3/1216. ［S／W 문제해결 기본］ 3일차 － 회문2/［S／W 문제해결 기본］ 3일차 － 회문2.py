def solution(board):
    answer = 1
    for line in board:
        for length in range(2, 101):
            for idx in range(100 - length + 1):
                string = line[idx : idx + length + 1]
                if string == string[::-1]:
                    answer = max(answer, len(string))

    new_board = list(zip(*board))
    for line in new_board:
        for length in range(2, 101):
            for idx in range(100 - length + 1):
                string = line[idx : idx + length + 1]
                if string == string[::-1]:
                    answer = max(answer, len(string))

    return answer

T = 1
for _ in range(T):
    seq = int(input())
    board = [list(input().rstrip()) for _ in range(100)]
    print(f'#{seq} {solution(board)}')