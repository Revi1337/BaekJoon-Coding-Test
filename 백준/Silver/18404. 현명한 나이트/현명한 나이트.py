def solution(N, M, X, Y, E):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    dist = [[-1] * N for _ in range(N)]
    dist[X - 1][Y - 1], stack = 0, [[X - 1, Y - 1]]
    left = set((row - 1, col - 1) for row, col in E)

    while stack:
        row, col = stack.pop(0)
        if (row, col) in left:
            left.discard((row, col))
        if not left:
            print(*[dist[r - 1][c - 1] for r, c in E])
            return
        for nrow, ncol in [row - 2, col - 1], [row - 2, col + 1], [row - 1, col - 2], [row - 1, col + 2], [row + 1, col - 2], [row + 1, col + 2], [row + 2, col - 1], [row + 2, col + 1]:
            if not inside(nrow, ncol) or dist[nrow][ncol] != -1:
                continue
            dist[nrow][ncol] = dist[row][col] + 1
            stack.append([nrow, ncol])

N, M = map(int, input().split())
X, Y = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, X, Y, E)
