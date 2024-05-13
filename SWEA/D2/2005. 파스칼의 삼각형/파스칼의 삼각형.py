def solution(idx, N):
    entry = 3
    init = [[0] * offset for offset in range(3, 3 + N)]
    init[0][entry // 2] = 1
    for row in range(1, len(init)):
        for col in range(1, len(init[row]) - 1):
            init[row][col] = init[row - 1][col - 1] + init[row - 1][col]
    print(f'#{idx}')
    for line in init:
        print(*filter(lambda x: x != 0, line))

T = int(input())
for idx in range(T):
    N = int(input())
    solution(idx + 1, N)