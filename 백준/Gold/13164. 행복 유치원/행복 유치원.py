def solution(N, K, heights):
    diff = [0] * (N - 1)
    for idx in range(N - 1):
        diff[idx] = heights[idx + 1] - heights[idx]

    diff.sort()
    return sum(diff[:N - K])

N, K = map(int, input().split())
heights = list(map(int, input().split()))
print(solution(N, K, heights))