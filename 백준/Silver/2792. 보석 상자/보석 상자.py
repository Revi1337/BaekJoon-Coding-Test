import sys

input = sys.stdin.readline

def solution(n, m, colors):
    colors.sort()
    left, right = 1, colors[-1]
    while left <= right:
        mid = (left + right) // 2
        counter = 0
        for capacity in colors:
            if capacity % mid == 0:
                counter += (capacity // mid)
            else:
                counter += (capacity // mid) + 1
        if counter > n:
            left = mid + 1
        else:
            right = mid - 1
    return left


n, m = map(int, input().split())
colors = [int(input().rstrip()) for _ in range(m)]
print(solution(n, m, colors))