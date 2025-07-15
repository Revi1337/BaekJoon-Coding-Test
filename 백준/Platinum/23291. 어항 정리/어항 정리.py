drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
EMPTY = float('inf')

def solution(N, K, narr):

    def increase(arr):
        mn = min(narr)
        for col in range(N):
            if narr[col] == mn:
                narr[col] += 1
        return arr

    def fill(arr):
        size = len(arr)
        narr = [[EMPTY] * (size - 1) for _ in range(2)]
        narr[0][0] = arr[0]
        for col in range(1, size):
            narr[1][col - 1] = arr[col]
        return narr

    def rotate(arr):
        return [list(row) for row in zip(*arr[::-1])]

    def above(arr):
        while True:
            rsize, csize, ecol = len(arr), len(arr[-1]), len(arr[-1])
            for col in range(csize):
                if arr[0][col] == EMPTY:
                    ecol = col
                    break

            if ecol + rsize - 1 > csize - 1:
                return arr

            left, right = [], arr[-1][ecol:]
            for row in range(rsize):
                l = [arr[row][col] for col in range(ecol)]
                left.append(l)

            left = rotate(left)
            arr, diff = [], len(right) - len(left[0])
            for l in left:
                l.extend([EMPTY] * diff)
                arr.append(l)
            arr.append(right)

    def control(arr):
        rsize, csize = len(arr), len(arr[-1])
        costs = {}
        for row in range(rsize):
            for col in range(csize):
                if arr[row][col] == EMPTY:
                    continue
                for d in range(4):
                    nrow, ncol = row + drow[d], col + dcol[d]
                    if 0 <= nrow < rsize and 0 <= ncol < csize and arr[nrow][ncol] != EMPTY:
                        if (row, col) < (nrow, ncol):
                            diff = abs(arr[row][col] - arr[nrow][ncol]) // 5
                            if diff > 0:
                                if arr[row][col] > arr[nrow][ncol]:
                                    costs[(row, col)] = costs.get((row, col), 0) - diff
                                    costs[(nrow, ncol)] = costs.get((nrow, ncol), 0) + diff
                                else:
                                    costs[(nrow, ncol)] = costs.get((nrow, ncol), 0) - diff
                                    costs[(row, col)] = costs.get((row, col), 0) + diff

        for (row, col), cost in costs.items():
            arr[row][col] = max(arr[row][col] + cost, 0)

    def flat(arr):
        rsize, csize, ecol = len(arr), len(arr[-1]), len(arr[-1])
        for col in range(csize):
            if arr[0][col] == EMPTY:
                ecol = col
                break
        narr = []
        for col in range(ecol):
            lst = [arr[row][col] for row in range(rsize - 1, -1, -1) if arr[row][col] != EMPTY]
            narr.extend(lst)
        narr.extend(arr[-1][ecol:])
        return narr

    def above2(arr):
        half = len(arr) // 2
        arr = [arr[:half][::-1], arr[half:]]

        left, right = [[] for _ in range(2)]
        for lst in arr:
            half = len(lst) // 2
            left.append(lst[:half])
            right.append(lst[half:])

        rsize, csize = len(left), len(left[-1])
        nleft = [[0] * csize for _ in range(rsize)]
        for row in range(rsize):
            for col in range(csize):
                nleft[rsize - row - 1][csize - col - 1] = left[row][col]

        return [*nleft, *right]

    cnt = 0
    while True:
        if max(narr) - min(narr) <= K:
            return cnt
        cnt += 1

        narr = increase(narr)
        narr = fill(narr)
        narr = above(narr)
        control(narr)
        narr = flat(narr)

        narr = above2(narr)
        control(narr)
        narr = flat(narr)

N, K = map(int, input().split())
board = list(map(int, input().split()))
print(solution(N, K, board))
