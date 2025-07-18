drow = [0, -1, -1]
dcol = [-1, -1, 0]

def solution(M, N, grows):
    acc = [0] * (2 * M - 1)

    for z, o, t in grows:
        idx = 0
        for _ in range(z): idx += 1
        for _ in range(o): acc[idx] += 1; idx += 1
        for _ in range(t): acc[idx] += 2; idx += 1

    I = [*range(M * (M - 1), -1, -M), *range(1, M)]
    B = [[1] * M for _ in range(M)]

    for i in range(2 * M - 1):
        r, c = I[i] // M, I[i] % M
        B[r][c] += acc[i]

    for col in range(1, M):
        B[1][col] += max(B[1 + drow[d]][col + dcol[d]] - 1 for d in range(3))

    print(*B[0], sep = ' ')
    for row in range(1, M):
        print(B[row][0], end = ' ')
        print(*B[1][1:], sep = ' ')

M, N = map(int, input().split())
grows = [list(map(int, input().split())) for _ in range(N)]
solution(M, N, grows)