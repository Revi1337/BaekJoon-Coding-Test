def solution(count, heights):
    for cnt in range(count):
        minH, maxH = min(heights), max(heights)
        if minH != maxH:
            minIdx, maxIdx = heights.index(minH), heights.index(maxH)
            heights[minIdx] += 1
            heights[maxIdx] -= 1

    return max(heights) - min(heights)

T = 10
for seq in range(T):
    count = int(input())
    heights = list(map(int, input().split()))
    print(f'#{seq + 1} {solution(count, heights)}')