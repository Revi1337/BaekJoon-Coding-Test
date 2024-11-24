def solution(board):

    def is_pal(b, length):
        for line in b:
            for idx in range(100 - length + 1):
                if line[idx : idx + length] == line[idx : idx + length][::-1]:
                    return True
        return False

    new_board = list(zip(*board))
    for length in range(100, 1, -1):
        if is_pal(board, length) or is_pal(new_board, length):
            return length

    return 1

T = 10
for _ in range(T):
    seq = int(input())
    board = [list(input().rstrip()) for _ in range(100)]
    print(f'#{seq} {solution(board)}')