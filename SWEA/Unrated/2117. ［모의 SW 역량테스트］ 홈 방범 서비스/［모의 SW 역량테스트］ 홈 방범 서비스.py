drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, board):
    h = set()
    for row in range(N):
        for col in range(N):
            if board[row][col]:
                h.add((row, col))

    answer = 0
    for size in range(1, N + 2):
        cost = (size * size) + ((size -  1) ** 2)
        k = size
        for row in range(N):
            for col in range(N):
                hcnt = 0
                for dr in range(-(k - 1), k):
                    nr = row + dr
                    if 0 <= nr < N:
                        delta = (k - 1) - abs(dr)
                        for dc in range(-delta, delta + 1):
                            nc = col + dc
                            if 0 <= nc < N and board[nr][nc] == 1:
                                hcnt += 1

                if (hcnt * M) - cost >= 0:
                    answer = max(answer, hcnt)

    return answer

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t} {solution(N, M, board)}')