def solution(N, board):
    mid = N // 2
    answer = sum(board[mid])
    init = 0

    while init < mid:
        answer += sum(board[init][mid - init : mid + init + 1])
        answer += sum(board[N - init - 1][mid - init: mid + init + 1])
        init += 1

    return answer

T = int(input())
for seq in range(T):
    N = int(input())
    board = [list(map(int, input().rstrip())) for _ in range(N)]
    print(f'#{seq + 1} {solution(N, board)}')
