def solution(N, B, arr):

    MOD = 1000

    def mul(A, B):
        arr = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                tmp = 0
                for k in range(N):
                    tmp += A[i][k] * B[k][j]
                arr[i][j] = tmp % MOD

        return arr

    def power(arr, exp):
        if exp == 1:
            return [[val % MOD for val in row] for row in arr]

        half = power(arr, exp // 2)
        result = mul(half, half)

        if exp % 2 == 1:
            result = mul(result, arr)

        return result


    result = power(arr, B)
    for line in result:
        print(*line)

N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
solution(N, B, arr)