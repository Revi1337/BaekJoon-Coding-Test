def solution(board, moves):
    basket = []
    length = len(board)
    answer = 0
    for move in moves:
        for idx in range(length):
            if board[idx][move - 1] != 0:
                value = board[idx][move - 1]
                if basket and basket[-1] == value:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(value)
                board[idx][move - 1] = 0
                break
    return answer