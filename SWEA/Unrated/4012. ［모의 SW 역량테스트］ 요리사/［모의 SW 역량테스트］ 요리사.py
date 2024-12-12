def solution(N, board):

    def backtracking(n, alst, blst):
        if n == N:
            if len(alst) == (N // 2):
                asum = bsum = 0
                for i in range(n // 2):
                    for j in range(n // 2):
                        asum += board[alst[i]][alst[j]]
                        bsum += board[blst[i]][blst[j]]
                nonlocal answer
                answer = min(answer, abs(asum - bsum))
            return

        alst.append(n)
        backtracking(n + 1, alst, blst)
        alst.pop()

        blst.append(n)
        backtracking(n + 1, alst, blst)
        blst.pop()

    answer = 20000 * pow(N, 2)
    backtracking(0, [], [])

    return answer

T = int(input())
for seq in range(T):
    N = int(input())
    board = [list(map(int,  input().split())) for _ in range(N)]
    print(f'#{seq + 1} {solution(N, board)}')
