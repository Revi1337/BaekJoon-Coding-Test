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

    B = [[[1, 1] for _ in range(M)] for _ in range(M)]
    for gg in G:
        for idx in range(len(gg)):
            val = gg[idx]
            ridx, cidx = I[idx] // M, I[idx] % M
            B[ridx][cidx][0], B[ridx][cidx][1] = B[ridx][cidx][1], B[ridx][cidx][1] + val

        for row in range(1, M):
            for col in range(1, M):
                mx = max(B[row + drow[d]][col + dcol[d]][1] - B[row + drow[d]][col + dcol[d]][0] for d in range(3))
                B[row][col][0], B[row][col][1] = B[row][col][1], B[row][col][1] + mx

    for line in B:
        print(*[entry[1] for entry in line], sep = ' ')


M, N = map(int, input().split())
grows = [list(map(int, input().split())) for _ in range(N)]
solution(M, N, grows)