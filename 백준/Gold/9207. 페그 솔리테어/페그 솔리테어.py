dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solution(board):

    def backtracking(cnt):
        nonlocal ans1, ans2
        pins = [(row, col) for row in range(1, 6) for col in range(1, 10) if board[row][col] == 'o']
        if len(pins) < ans1:
            ans2 = cnt
            ans1 = len(pins)

        for sr, sc in pins:
            for d in range(4):
                nr, nc = sr + dr[d], sc + dc[d]
                if 1 <= nr < 6 and 1 <= nc < 10:
                    if board[nr][nc] == 'o' and board[nr + dr[d]][nc + dc[d]] == '.':
                        board[sr][sc] = board[nr][nc] = '.'
                        board[nr + dr[d]][nc + dc[d]] = 'o'
                        backtracking(cnt + 1)
                        board[sr][sc] = board[nr][nc] = 'o'
                        board[nr + dr[d]][nc + dc[d]] = '.'

    board.insert(0, ['#'] * 11)
    board.append(['#'] * 11)
    ans1 = ans2 = 10

    backtracking(0)
    print(ans1, ans2, sep = ' ')

N = int(input())
for _ in range(N):
    board = [['#'] + list(input().rstrip()) + ['#'] for _ in range(5)]
    if _ != N - 1:
        input()
    solution(board)