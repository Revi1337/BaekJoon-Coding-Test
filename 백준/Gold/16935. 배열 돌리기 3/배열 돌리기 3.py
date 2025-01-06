def solution(N, M, R, array, opers):

    def first(arr):
        return arr[::-1]

    def second(arr):
        return [row[::-1] for row in arr]

    def third(arr):
        N, M = len(arr), len(arr[0])
        carr = [[0] * N for _ in range(M)]
        for row in range(N):
            for col in range(M):
                carr[col][N - row - 1] = arr[row][col]
        return carr

    def four(arr):
        N, M = len(arr), len(arr[0])
        carr = [[0] * N for _ in range(M)]
        for row in range(N):
            for col in range(M):
                carr[M - col - 1][row] = arr[row][col]
        return carr

    def five(arr):
        N, M = len(arr), len(arr[0])
        carr = [[0] * M for _ in range(N)]
        hn, hm = N // 2, M // 2
        for row in range(N):
            for col in range(M):
                if row < hn and col < hm:
                    carr[row][col + hm] = arr[row][col]
                elif row < hn and col >= hm:
                    carr[row + hn][col] = arr[row][col]
                elif row >= hn and col < hm:
                    carr[(row + hn) % N][col] = arr[row][col]
                elif row >= hn and col >= hm:
                    carr[row][(col + hm) % M] = arr[row][col]
        return carr

    def six(arr):
        N, M = len(arr), len(arr[0])
        carr = [[0] * M for _ in range(N)]
        hn, hm = N // 2, M // 2
        for row in range(N):
            for col in range(M):
                if row < hn and col < hm:
                    carr[(row + hn) % N][col] = arr[row][col]
                elif row < hn and col >= hm:
                    carr[row][(col + hm) % M] = arr[row][col]
                elif row >= hn and col < hm:
                    carr[row][col + hm] = arr[row][col]
                elif row >= hn and col >= hm:
                    carr[(row + hn) % N][col] = arr[row][col]
        return carr

    callables = [0, first, second, third, four, five, six]
    for oper in opers:
        callable = callables[oper]
        array = callable(array)

    for line in array:
        print(*line)

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
opers = list(map(int, input().split()))
solution(N, M, R, arr, opers)
