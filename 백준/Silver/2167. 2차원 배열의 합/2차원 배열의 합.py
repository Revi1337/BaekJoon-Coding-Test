import sys

input = sys.stdin.readline

def solution(n, m, arr, require):
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            prefix_sum[row][col] = prefix_sum[row - 1][col] \
                                   + prefix_sum[row][col - 1] \
                                   - prefix_sum[row - 1][col - 1] \
                                   + arr[row - 1][col - 1]

    for r1, c1, r2, c2 in require:
        print(prefix_sum[r2][c2] - prefix_sum[r2][c1 - 1] - prefix_sum[r1 - 1][c2] + prefix_sum[r1 - 1][c1 - 1])

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
count = int(input().rstrip())
require = [list(map(int, input().split())) for _ in range(count)]
solution(n, m, arr, require)
