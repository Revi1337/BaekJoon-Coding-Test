def solution(N, board):

    def backtracking(n, scnt, lcnt, slst, llst):
        if n == N:
            if scnt == (N // 2) and lcnt == (N // 2):
                sm1 = sm2 = 0
                for idx in range(N // 2):
                    for rdx in range(N // 2):
                        sm1 += board[slst[idx]][slst[rdx]]
                        sm2 += board[llst[idx]][llst[rdx]]
                nonlocal answer
                answer = min(answer, abs(sm1 - sm2))
            return
        backtracking(n + 1, scnt + 1, lcnt, slst + [n], llst)
        backtracking(n + 1, scnt, lcnt + 1, slst, llst + [n])

    answer = 1e9
    backtracking(0, 0, 0, [], [])

    return answer

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))