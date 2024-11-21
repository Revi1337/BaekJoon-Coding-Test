def solution(board):
    for line in board:
        line.insert(0, 0)
        line.append(0)

    end = None
    for row in range(100):
        for col in range(102):
            if board[row][col] == 2:
                end = [row, col]
                break

    possible = []
    for col in range(102):
        if board[0][col] == 1:
            possible.append([0, col])

    for poss in possible:
        curr = [poss[0], poss[1]]

        while curr[0] < 100:
            if board[curr[0]][curr[1] - 1] == 1:  # 왼쪽 이동 가능
                while board[curr[0]][curr[1] - 1] == 1:
                    curr[1] -= 1
            elif board[curr[0]][curr[1] + 1] == 1:  # 오른쪽 이동 가능
                while board[curr[0]][curr[1] + 1] == 1:
                    curr[1] += 1
            curr[0] += 1 # 아래로 이동

        if curr[1] == end[1]:
            return poss[1] - 1

T = 10
for _ in range(T):
    seq = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{seq} {solution(board)}')