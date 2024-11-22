def solution(board):
    for line in board:
        line.insert(0, 0)
        line.append(0)

    possible = []
    for col in range(102):
        if board[0][col] == 1:
            possible.append([0, col])

    answer = -1
    min_cnt = 1e9
    for poss in possible:
        curr = [*poss]
        counter = 0
        
        while curr[0] < 100:
            if board[curr[0]][curr[1] - 1] == 1:
                while board[curr[0]][curr[1] - 1] == 1:
                    curr[1] -= 1
                    counter += 1
            elif board[curr[0]][curr[1] + 1] == 1:
                while board[curr[0]][curr[1] + 1] == 1:
                    counter += 1
                    curr[1] += 1
            curr[0] += 1
            counter += 1

        if counter < min_cnt:
            min_cnt = counter
            answer = poss[1] - 1

    return answer

T = 10
for _ in range(T):
    seq = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{seq} {solution(board)}')