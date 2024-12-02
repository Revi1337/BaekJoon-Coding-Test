from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, board):
    ans_val = 1
    ans_counter = 1
    check = [[0] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if check[row][col]:
                continue

            check[row][col] = 1
            queue = deque([(row, col)])
            node_val, counter = board[row][col], 1
            while queue:
                r, c = queue.popleft()
                for d in range(4):
                    nr, nc = r + drow[d], c + dcol[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        if abs(board[r][c] - board[nr][nc]) == 1 and not check[nr][nc]:
                            check[nr][nc] = 1
                            queue.append((nr, nc))
                            node_val = min(node_val, board[nr][nc])
                            counter += 1

            if counter > ans_counter:
                ans_val, ans_counter = node_val, counter
            elif counter == ans_counter:
                ans_val = min(ans_val, node_val)

    return f'{ans_val} {ans_counter}'


T = int(input())
for seq in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{seq + 1} {solution(N, board)}')

