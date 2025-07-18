drow = [0, -1, -1]
dcol = [-1, -1, 0]

def solution(M, N, grows):
    I = [*range(M * (M - 1), -1, -M), *range(1, M)]
    G = []
    for grow in grows:
        gg = []
        for g, v in enumerate(grow):
            gg.extend([g] * v)
        G.append(gg)

    B = [[1] * M for _ in range(M)]
    for gg in G:
        for idx in range(len(gg)):
            val = gg[idx]
            ridx, cidx = I[idx] // M, I[idx] % M
            B[ridx][cidx] += val

    for row in range(1, M):
        for col in range(1, M):
            B[row][col] += max(B[row + drow[d]][col + dcol[d]] - 1 for d in range(3))

    for line in B:
        print(*line, sep = ' ')


M, N = map(int, input().split())
grows = [list(map(int, input().split())) for _ in range(N)]
solution(M, N, grows)