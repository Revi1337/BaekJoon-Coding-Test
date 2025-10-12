def solution(N, M, H):
    acc = [[*line, 0] for line in H]
    acc.append([0] * len(acc[0]))

    for col in range(N + 1):
        for row in range(N, 0, -1):
            acc[row][col] -= acc[row - 1][col]

    for row in range(N + 1):
        for col in range(N, 0, -1):
            acc[row][col] -= acc[row][col - 1]

    half = M // 2
    ans = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            center = 0
            if row >= half and col >= half:
                center = -acc[row - half][col - half]

            top = 0
            if row >= M:
                top = ans[row - M][col]

            left = 0
            if col >= M:
                left = ans[row][col - M]

            top_left_dup = 0
            if row >= M and col >= M:
                top_left_dup = ans[row - M][col - M]

            ans[row][col] = center + top + left - top_left_dup

    for row in ans:
        print(*row)

N, M = map(int, input().split())
H = [list(map(int, input().split())) for _ in range(N)]
solution(N, M, H)
