def solution(idx, N, K, board):
    lst = []
    for col in range(N):
        lst.append("".join(map(str, [tmp[col] for tmp in board])))
        lst.append("".join(map(str, board[col])))
    answer = 0
    for string in lst:
        tmp = string.split('0')
        for seq in tmp:
            if sum(map(int, list(seq))) == K:
                answer += 1
    return f'#{idx} {answer}'

T = int(input())
for idx in range(T):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(solution(idx + 1, N, K, board))