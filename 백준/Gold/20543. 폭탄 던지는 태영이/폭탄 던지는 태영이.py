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
            center = -acc[row - half][col - half] if row >= half and col >= half else 0
            top = ans[row - M][col] if row >= M else 0
            left = ans[row][col - M] if col >= M else 0
            top_left_dup = ans[row - M][col - M] if row >= M and col >= M else 0

            ans[row][col] = center + top + left - top_left_dup

    for row in ans:
        print(*row)

N, M = map(int, input().split())
H = [list(map(int, input().split())) for _ in range(N)]
solution(N, M, H)