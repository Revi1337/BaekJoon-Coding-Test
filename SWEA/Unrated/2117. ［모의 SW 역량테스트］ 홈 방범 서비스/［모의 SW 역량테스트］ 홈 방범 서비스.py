drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

from collections import deque

def solution(N, M, board):
    h = set()
    for row in range(N):
        for col in range(N):
            if board[row][col]:
                h.add((row, col))

    answer = 0
    for size in range(1, N + 2):
        cost = (size * size) + ((size -  1) ** 2)
        for row in range(N):
            for col in range(N):
                limit = size - 1
                check = {(row, col)}
                queue = deque([(row, col)])
                hcnt = 1 if board[row][col] else 0

                while limit > 0:
                    for _ in range(len(queue)):
                        r, c = queue.popleft()
                        for d in range(4):
                            nrow, ncol = r + drow[d], c + dcol[d]
                            if 0 <= nrow < N and 0 <= ncol < N and (nrow, ncol) not in check:
                                queue.append((nrow, ncol))
                                check.add((nrow, ncol))
                                if board[nrow][ncol]:
                                    hcnt += 1
                    limit -= 1

                if (hcnt * M) - cost >= 0:
                    answer = max(answer, hcnt)

    return answer

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t} {solution(N, M, board)}')
