import sys

input = sys.stdin.readline

def solution(n, k, sizes):
    max_size = max(sizes)
    left, right = 1, max_size
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        counter = 0
        for size in sizes:
            counter += (size // mid)
        if counter >= k:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

n, k = map(int, input().split())
sizes = [int(input().rstrip()) for _ in range(n)]
print(solution(n, k, sizes))
