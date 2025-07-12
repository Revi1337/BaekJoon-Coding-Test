def solution(N, L, R, X, nums):

    MN, MX = 1, 1_000_000

    def backtrack(n, sm, d1, d2):
        if sm > R:
            return

        if n == N:
            if L <= sm <= R and d2 - d1 >= X:
                nonlocal ans
                ans += 1
            return

        backtrack(n + 1, sm + nums[n], min(d1, nums[n]), max(d2, nums[n]))
        backtrack(n + 1, sm, d1, d2)

    ans = 0
    backtrack(0, 0, MX, MN)

    return ans


N, L, R, X = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(N, L, R, X, nums))