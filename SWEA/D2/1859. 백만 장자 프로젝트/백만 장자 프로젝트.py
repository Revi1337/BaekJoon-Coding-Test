def solution(N, prices):
    answer = start = 0
    while start < N:
        max_idx = start
        for idx in range(start + 1, N):
            if prices[idx] > prices[max_idx]:
                max_idx = idx
        for idx in range(start, max_idx + 1):
            answer += prices[max_idx] - prices[idx]
        start = max_idx + 1

    return answer

T = int(input())
for seq in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    print(f'#{seq + 1} {solution(N, prices)}')