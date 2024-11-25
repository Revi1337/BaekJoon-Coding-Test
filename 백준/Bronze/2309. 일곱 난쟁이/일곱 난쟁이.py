def solution(heights):
    N = 9
    target_height = 100
    total = sum(heights)
    heights.sort()

    for i in range(N - 1):
        for j in range(N):
            if total - heights[i] - heights[j] == target_height:
                for idx in range(N):
                    if idx != i and idx != j:
                        print(heights[idx])
                return

heights = [int(input().rstrip()) for _ in range(9)]
solution(heights)
