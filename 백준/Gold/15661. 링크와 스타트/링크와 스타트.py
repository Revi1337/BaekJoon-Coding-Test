import sys

input = sys.stdin.readline

def solution(N, arr):

    def backtrack(n, left, right, lsm, rsm):
        nonlocal ans
        if ans == 0:
            return
        if n == N:
            if right:
                diff = abs(lsm - rsm)
                if diff < ans:
                    ans = diff
            return

        left.append(n)
        backtrack(n + 1, left, right, lsm + sum(cache[n][m] for m in left), rsm)
        left.pop()

        right.append(n)
        backtrack(n + 1, left, right, lsm, rsm + sum(cache[n][m] for m in right))
        right.pop()

    cache = [[0] * N for _ in range(N)]
    for idx in range(N):
        for jdx in range(N):
            cache[idx][jdx] = arr[idx][jdx] + arr[jdx][idx]

    ans = 100 * (N ** 2)
    backtrack(1, [0], [], 0, 0)

    return ans

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))