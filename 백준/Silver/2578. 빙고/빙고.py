def solution(board, numbers):
    numbers = [num for line in numbers for num in line]
    lru = [[0] * 5 for _ in range(5)]

    for idx in range(25):
        num = numbers[idx]
        for row in range(5):
            for col in range(5):
                if board[row][col] == num:
                    lru[row][col] = 1

                    bing_cnt = 0
                    if sum([lru[c][c] for c in range(5)]) == 5:
                        bing_cnt += 1
                    if sum([lru[c][5 - c - 1] for c in range(5)]) == 5:
                        bing_cnt += 1

                    for c in range(5):
                        r = c
                        if sum(lru[r]) == 5:
                            bing_cnt += 1
                        if sum([cache[c] for cache in lru]) == 5:
                            bing_cnt += 1

                        if bing_cnt >= 3:
                            return idx + 1

board = [list(map(int, input().split())) for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]
print(solution(board, numbers))