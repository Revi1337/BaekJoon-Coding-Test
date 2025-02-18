def solution(N, K, items):
    items.insert(0, [0, 0])
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for idx in range(1, N + 1):
        w, v = items[idx]
        for bag in range(1, K + 1):
            if w <= bag:
                dp[idx][bag] = max(dp[idx - 1][bag], dp[idx - 1][bag - w] + items[idx][1])
            else:
                dp[idx][bag] = dp[idx - 1][bag]

    return max(dp[-1])

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, K, items))
