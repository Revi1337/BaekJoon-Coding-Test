drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

def solution(idx, N):
    d = 0
    answer = [[0] * N for _ in range(N)]
    init = 1

    direction = [0, 0]
    answer[0][0] = init
    init += 1

    while init <= N ** 2:
        nrow, ncol = direction[0] + drow[d], direction[1] + dcol[d]
        if (0 <= nrow < N) and (0 <= ncol < N) and (not answer[nrow][ncol]):
            answer[nrow][ncol] = init
            direction = [nrow, ncol]
            init += 1
        else:
            d = (d + 1) % 4

    print(f'#{idx}')
    for line in answer:
        print(*line)

T = int(input())
for idx in range(T):
    N = int(input())
    solution(idx + 1, N)