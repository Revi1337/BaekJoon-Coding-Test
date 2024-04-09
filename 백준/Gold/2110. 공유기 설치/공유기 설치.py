import sys

input = sys.stdin.readline

def solution(n, c, position):
    answer = 0
    position.sort()
    left, right = 1, position[-1] - position[0]
    while left <= right:
        mid = (left + right) // 2
        prev = position[0]
        counter = 1
        for idx in range(1, n):
            if position[idx] - prev >= mid:
                prev = position[idx]
                counter += 1
        if counter >= c:
            if answer < mid:
                answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

n, c = map(int, input().split())
position = [int(input().rstrip()) for _ in range(n)]
print(solution(n, c, position))