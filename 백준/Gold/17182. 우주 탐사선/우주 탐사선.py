def solution(N, K, arr):
    for mid in range(N):
        for st in range(N):
            for end in range(N):
                if arr[st][mid] + arr[mid][end] < arr[st][end]:
                    arr[st][end] = arr[st][mid] + arr[mid][end]

    def backtracking(n, prev, sm):
        if n == N:
            nonlocal answer
            answer = min(answer, sm)
            return

        for v in range(N):
            if not check[v]:
                check[v] = 1
                backtracking(n + 1, v, sm + arr[prev][v])
                check[v] = 0

    answer = 1000 * (N - 1)
    check = [0] * N
    check[K] = 1
    backtracking(1, K, 0)

    return answer


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, K, arr))