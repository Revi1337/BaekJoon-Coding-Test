def solution(seq, length, board):
    counter = int(length // 2)
    answer = sum(board[counter])
    i = 0
    while counter > i:
        answer += sum(board[i][counter - i:counter + i + 1])
        answer += sum(board[length - i - 1][counter - i:counter + i + 1])
        i += 1

    return f"#{seq} {answer}"

T = int(input())
for seq in range(T):
    length = int(input())
    board = [list(map(int, input().rstrip())) for _ in range(length)]
    print(solution(seq + 1, length, board))
    