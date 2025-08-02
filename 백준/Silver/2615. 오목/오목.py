import sys

input = sys.stdin.readline

def solution(arr):

    SIZE, LIM = 19, 5

    inside = lambda row, col: 0 <= row < SIZE and 0 <= col < SIZE

    def extract(tmp):
        for lst in tmp:
            if len(lst) == LIM:
                lst.sort(key=lambda x: (x[1], x[0]))
                return lst
        return []

    def search_row(srow):
        scol, tmp = 0, []
        while inside(srow, scol):
            if arr[srow][scol] != 0:
                ncol, color, lst = scol, arr[srow][scol], []
                while inside(srow, ncol):
                    if arr[srow][ncol] == color:
                        lst.append([srow, ncol])
                    else:
                        break
                    ncol += 1
                scol = ncol
                if len(lst) >= LIM:
                    tmp.append(lst)
            else:
                scol += 1

        return extract(tmp)

    def search_col(scol):
        srow, tmp = 0, []
        while inside(srow, scol):
            if arr[srow][scol] != 0:
                nrow, color, lst = srow, arr[srow][scol], []
                while inside(nrow, scol):
                    if arr[nrow][scol] == color:
                        lst.append([nrow, scol])
                    else:
                        break
                    nrow += 1
                srow = nrow
                if len(lst) >= LIM:
                    tmp.append(lst)
            else:
                srow += 1

        return extract(tmp)

    def search_d1(srow, scol):
        if srow - scol > 0:
            srow, scol = srow - scol, 0
        elif srow - scol < 0:
            srow, scol = 0, scol - srow
        else:
            srow = scol = 0

        tmp = []
        while inside(srow, scol):
            if arr[srow][scol] != 0:
                nrow, ncol, color, lst = srow, scol, arr[srow][scol], []
                while inside(nrow, ncol):
                    if arr[nrow][ncol] == color:
                        lst.append([nrow, ncol])
                    else:
                        break
                    nrow, ncol = nrow + 1, ncol + 1
                srow, scol = nrow, ncol
                if len(lst) >= LIM:
                    tmp.append(lst)
            else:
                srow, scol = srow + 1, scol + 1

        return extract(tmp)

    def search_d2(srow, scol):
        srow, scol, tmp = min(srow, scol), max(srow, scol), []
        while inside(srow, scol):
            if arr[srow][scol] != 0:
                nrow, ncol, color, lst = srow, scol, arr[srow][scol], []
                while inside(nrow, ncol):
                    if arr[nrow][ncol] == color:
                        lst.append([nrow, ncol])
                    else:
                        break
                    nrow, ncol = nrow + 1, ncol - 1
                srow, scol = nrow, ncol
                if len(lst) >= LIM:
                    tmp.append(lst)
            else:
                srow, scol = srow + 1, scol - 1

        return extract(tmp)


    chr, chc = [[0] * SIZE for _ in range(2)]
    chd1, chd2 = [[0] * (SIZE * 2) for _ in range(2)]
    for row in range(SIZE):
        for col in range(SIZE):
            if not chr[row]:
                chr[row] = 1
                lst = search_row(row)
                if lst:
                    print(arr[lst[0][0]][lst[0][1]])
                    print(lst[0][0] + 1, lst[0][1] + 1, sep = ' ')
                    return
            if not chc[col]:
                chc[col] = 1
                lst = search_col(col)
                if lst:
                    print(arr[lst[0][0]][lst[0][1]])
                    print(lst[0][0] + 1, lst[0][1] + 1, sep=' ')
                    return
            if not chd1[row - col]:
                chd1[row - col] = 1
                lst = search_d1(row, col)
                if lst:
                    print(arr[lst[0][0]][lst[0][1]])
                    print(lst[0][0] + 1, lst[0][1] + 1, sep=' ')
                    return
            if not chd2[row + col]:
                chd2[row + col] = 1
                lst = search_d2(row, col)
                if lst:
                    print(arr[lst[0][0]][lst[0][1]])
                    print(lst[0][0] + 1, lst[0][1] + 1, sep=' ')
                    return

    print(0)

arr = [list(map(int, input().split())) for _ in range(19)]
solution(arr)