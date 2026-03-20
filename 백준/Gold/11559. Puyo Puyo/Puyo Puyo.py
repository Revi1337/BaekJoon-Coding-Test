drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(arr):

    inside = lambda row, col: 0 <= row < 12 and 0 <= col < 6

    ans = 0
    while True:
        check = [[0] * 6 for _ in range(12)]
        breaked = False
        for row in range(12):
            for col in range(6):
                if arr[row][col] != '.' and not check[row][col]:
                    color = arr[row][col]
                    queue = [(row, col)]
                    check[row][col] = 1
                    lst = [(row, col)]
                    while queue:
                        srow, scol = queue.pop()
                        for d in range(4):
                            nrow, ncol = srow + drow[d], scol + dcol[d]
                            if inside(nrow, ncol) and not check[nrow][ncol] and arr[nrow][ncol] == color:
                                check[nrow][ncol] = 1
                                queue.append((nrow, ncol))
                                lst.append((nrow, ncol))

                    if len(lst) >= 4:
                        breaked = True
                        for srow, scol in lst:
                            arr[srow][scol] = '.'

        if not breaked:
            return ans

        ans += 1

        for row in range(11, -1, -1):
            for col in range(6):
                if arr[row][col] != '.':
                    srow, scol = row, col
                    while True:
                        nrow = srow + 1
                        if nrow >= 12 or arr[nrow][scol] != '.':
                            break
                        arr[nrow][scol], arr[srow][scol] = arr[srow][scol], '.'
                        srow = nrow

arr = [list(input().rstrip()) for _ in range(12)]
print(solution(arr))

