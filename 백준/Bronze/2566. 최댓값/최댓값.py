table = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
max_row, max_col = 0, 0
for row in range(9):
    for col in range(9):
        if max_num <= table[row][col]:
            max_row = row + 1
            max_col = col + 1
            max_num = table[row][col]

print(max_num)
print(max_row, max_col)

# answer = 0
# row, col = 0, 0
#
# for idx in range(9):
#     rows = list(map(int, input().split()))
#     for j in range(len(rows)):
#         if rows[j] > answer:
#             answer = rows[j]
#             row, col = idx + 1, j + 1
#
# print(answer)
# print(row, col)