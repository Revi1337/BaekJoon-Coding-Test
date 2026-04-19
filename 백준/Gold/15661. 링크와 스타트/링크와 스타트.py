# 2026-04-19
# https://www.acmicpc.net/problem/15661
# 링크와 스타트
# V4. Backtracking (탐색 범위를 줄이자) + 간단히 컷엣지 + 캐싱

def solution(N, arr):

    def backtrack(n, lsum, rsum, left, right):
        nonlocal ans
        if ans == 0:
            return
        if n == N:
            if left and right:
                ans = min(ans, abs(lsum - rsum))
            return

        left.append(n)
        backtrack(n + 1, lsum + sum(cache[n][m] for m in left), rsum, left, right)
        left.pop()

        right.append(n)
        backtrack(n + 1, lsum, rsum + sum(cache[n][m] for m in right), left, right)
        right.pop()

    cache = [[0] * N for _ in range(N)]
    for n1 in range(N):
        for n2 in range(N):
            cache[n1][n2] = arr[n1][n2] + arr[n2][n1]

    ans = 100 * (N ** 2)
    backtrack(1, 0, 0, [0], [])

    return ans

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))
