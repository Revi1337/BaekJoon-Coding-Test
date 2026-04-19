# 2026-04-19
# https://www.acmicpc.net/problem/15661
# 링크와 스타트
# V3. Backtracking (탐색 범위를 줄이자) + 간단히 컷엣지

def solution(N, arr):

    def backtrack(n, left, right):
        nonlocal ans
        if ans == 0:
            return
        if n == N:
            if left and right:
                lsm = rsm = 0
                for idx in range(len(left)):
                    for jdx in range(idx + 1, len(left)):
                        lsm += arr[left[idx]][left[jdx]] + arr[left[jdx]][left[idx]]
                for idx in range(len(right)):
                    for jdx in range(idx + 1, len(right)):
                        rsm += arr[right[idx]][right[jdx]] + arr[right[jdx]][right[idx]]
                ans = min(ans, abs(lsm - rsm))
            return

        left.append(n)
        backtrack(n + 1, left, right)
        left.pop()

        right.append(n)
        backtrack(n + 1, left, right)
        right.pop()

    ans = 100 * (N ** 2)
    backtrack(1, [0], [])

    return ans

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))