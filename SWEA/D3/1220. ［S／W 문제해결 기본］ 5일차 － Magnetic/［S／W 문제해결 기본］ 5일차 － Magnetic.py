def solution(length, board):
    answer = 0
    board = list(zip(*board))
    for lst in board:
        prev = 0
        for n in lst:
            if n:
                if n == 2 and prev == 1:
                    answer += 1
                prev = n

    return answer

T = 10
for seq in range(T):
    length = int(input())
    board = [list(map(int, input().split())) for _ in range(length)]
    print(f'#{seq + 1} {solution(length, board)}')
