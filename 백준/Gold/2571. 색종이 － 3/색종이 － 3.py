def largest(heights):
    stack = []
    mx = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] >= h:
            H = heights[stack.pop()]
            W = i if not stack else i - stack[-1] - 1
            mx = max(mx, H * W)
        stack.append(i)
    heights.pop()
    return mx

def solution(N, edges):
    paper = [[0] * 100 for _ in range(100)]
    for col, row in edges:
        for r in range(row, row + 10):
            for c in range(col, col + 10):
                paper[r][c] = 1

    mx = 0
    heights = [0] * 100
    for r in range(100):
        for c in range(100):
            if paper[r][c]:
                heights[c] += 1
            else:
                heights[c] = 0

        mx = max(mx, largest(heights))

    return mx

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, edges))