def solution(N, K, board):
    rev_board = list(map(list, zip(*board)))

    def count(board):
        counter = 0
        for line in board:
            possible = 0
            for idx in range(N):
                if line[idx] == 1:
                    possible += 1
                else:
                    if possible == K:
                        counter += 1
                    possible = 0
            if possible == K:
                counter += 1
        return counter

    answer = count(board) + count(rev_board)
    return answer


T = int(input())
for seq in range(T):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{seq + 1} {solution(N, K, board)}')
