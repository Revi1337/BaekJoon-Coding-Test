import sys

input = sys.stdin.readline

def solution(N, M, board):
    max_length = min(N, M)
    answer = 0
    for length in range(1, max_length + 1):
        for row in range(N):
            for col in range(M):
                if (row + length <= N) and (col + length <= M):
                    tmp = {board[row][col]}
                    for (nr, nc) in (row, col + length - 1), (row + length - 1, col), (row + length - 1, col + length - 1):
                        tmp.add(board[nr][nc])
                    if len(tmp) == 1:
                        answer = max(answer, length)
    return answer ** 2

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
print(solution(N, M, board))
