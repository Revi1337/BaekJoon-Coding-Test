import sys

input = sys.stdin.readline

def solution(N, board):

    def recursive(level, board):
        if level == 1:
            nonlocal answer
            answer = board[0][0]
            return

        new_board = []
        for row in range(0, level, 2):
            lst = []
            for col in range(0, level, 2):
                pre = [board[row][col]]
                for r, c in (0, 1), (1, 1), (1, 0):
                    pre.append(board[row + r][col + c])
                pre.sort()
                lst.append(pre[-2])
            new_board.append(lst)
        recursive(level // 2, new_board)

    answer = None
    recursive(N, board)

    return answer

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))