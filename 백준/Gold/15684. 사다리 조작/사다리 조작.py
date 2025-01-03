# TODO 혼자못품. 다시풀어봐야함. 거의다 풀었는데.. 아쉽

def solution(N, M, H, edges):
    board = [[0] * (N + 2) for _ in range(H + 1)]
    for a, b in edges:
        board[a][b] = 1

    poss, poss_length = [], 0
    for row in range(1, H + 1):
        for col in range(1, N + 1):
            if not board[row][col]:
                poss.append((row, col))
                poss_length += 1

    def check():
        for sj in range(1, N + 1):
            j = sj
            for i in range(1, H + 1):
                if board[i][j] == 1:
                    j += 1
                elif board[i][j - 1] == 1:
                    j -= 1
            if j != sj:
                return 0
        return 1

    def backtracking(n, s):
        nonlocal ans
        if ans == 1:
            return

        if n == cnt:
            if check():
                ans = 1
            return

        for j in range(s, poss_length):
            ti, tj = poss[j]
            if board[ti][tj - 1] == 0 and board[ti][tj + 1] == 0:
                board[ti][tj] = 1
                backtracking(n + 1, j + 1)
                board[ti][tj] = 0

    for cnt in range(4):
        ans = 0
        backtracking(0, 0)
        if ans == 1:
            ans = cnt
            break
    else:
        ans = -1

    return ans

N, M, H = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, H, edges))