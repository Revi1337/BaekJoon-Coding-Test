def solution(H, W, pos):
    for line in pos:
        line.insert(0, '.')

    for row in range(H):
        for col in range(1, W + 1):
            if pos[row][col] == 'c':
                pos[row][col] = 0
            elif pos[row][col - 1] != '.':
                pos[row][col] = pos[row][col - 1] + 1

    for line in pos:
        for col in range(W + 1):
            if line[col] == '.':
                line[col] = -1

    for line in pos:
        print(*line[1:])


H, W = map(int, input().split())
pos = [list(input().rstrip()) for _ in range(H)]
solution(H, W, pos)
