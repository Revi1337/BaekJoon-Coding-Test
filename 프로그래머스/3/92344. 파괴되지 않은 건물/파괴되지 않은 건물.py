def solution(board, skill):
    n = len(board)
    m = len(board[0])
    acc = [[0] * (m + 1) for _ in range(n + 1)]

    for typ, r1, c1, r2, c2, degree in skill:
        val = -degree if typ == 1 else degree
        acc[r1][c1] += val
        acc[r1][c2 + 1] -= val
        acc[r2 + 1][c1] -= val
        acc[r2 + 1][c2 + 1] += val

    for j in range(m + 1):
        for i in range(1, n + 1):
            acc[i][j] += acc[i - 1][j]

    for i in range(n + 1):
        for j in range(1, m + 1):
            acc[i][j] += acc[i][j - 1]

    ans = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + acc[i][j] > 0:
                ans += 1
    return ans



# def solution(board, skill):
#     for t, r1 ,c1, r2, c2, deg in skill:
#         if t == 1:
#             for row in range(r1, r2 + 1):
#                 for col in range(c1, c2 + 1):
#                     board[row][col] -= deg
#         else:
#             for row in range(r1, r2 + 1):
#                 for col in range(c1, c2 + 1):
#                     board[row][col] += deg
                    
#     ans = 0
#     for row in range(len(board)):
#         for col in range(len(board[0])):
#             if board[row][col] > 0:
#                 ans += 1
#     return ans
