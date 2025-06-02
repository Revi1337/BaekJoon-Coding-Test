from collections import  deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, board):
    left = {(row, col) for row in range(N) for col in range(M) if board[row][col]}
    answer = 0

    while left:
        check = [[0 for _ in range(M)] for _ in range(N)]
        queue = deque([(0, 0)])
        check[0][0] = 1
        freq = {}

        while queue:
            row, col = queue.popleft()
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if 0 <= nrow < N and 0 <= ncol < M:
                    if board[nrow][ncol]:
                        freq[(nrow, ncol)] = freq.get((nrow, ncol), 0) + 1
                    elif not board[nrow][ncol] and not check[nrow][ncol]:
                        check[nrow][ncol] = 1
                        queue.append((nrow, ncol))

        for key, cnt in freq.items():
            if cnt >= 2:
                left.discard((key[0], key[1]))
                board[key[0]][key[1]] = 0
        answer += 1

    return answer

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))