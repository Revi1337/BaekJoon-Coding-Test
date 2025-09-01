import sys

input = sys.stdin.readline

def solution(N, arr):

    def backtrack(n, left, right):
        if n == N:
            if left and right:
                lsm = rsm = 0
                for idx in range(len(left)):
                    for jdx in range(idx + 1, len(left)):
                        lsm += arr[left[idx]][left[jdx]] + arr[left[jdx]][left[idx]]
                for idx in range(len(right)):
                    for jdx in range(idx + 1, len(right)):
                        rsm += arr[right[idx]][right[jdx]] + arr[right[jdx]][right[idx]]
                nonlocal ans
                ans = min(ans, abs(lsm - rsm))
            return

        left.append(n)
        backtrack(n + 1, left, right)
        left.pop()

        right.append(n)
        backtrack(n + 1, left, right)
        right.pop()

    ans = 100 * (N ** 2)
    backtrack(0, [], [])

    return ans

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))
