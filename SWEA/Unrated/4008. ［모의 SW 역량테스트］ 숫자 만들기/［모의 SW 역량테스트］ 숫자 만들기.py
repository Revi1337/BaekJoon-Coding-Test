def solution(N, opers, nums):

    def backtrack(n, sm):
        if n == N - 1:
            nonlocal mn, mx
            mn, mx = min(mn, sm), max(mx, sm)
            return

        if opers[0]:
            opers[0] -= 1
            backtrack(n + 1, sm + nums[n + 1])
            opers[0] += 1
        if opers[1]:
            opers[1] -= 1
            backtrack(n + 1, sm - nums[n + 1])
            opers[1] += 1
        if opers[2]:
            opers[2] -= 1
            backtrack(n + 1, sm * nums[n + 1])
            opers[2] += 1
        if opers[3]:
            opers[3] -= 1
            backtrack(n + 1, int(sm / nums[n + 1]))
            opers[3] += 1

    mn, mx = 1e9, -1e9
    backtrack(0, nums[0])

    return mx - mn


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    opers = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    print(f'#{t} {solution(N, opers, nums)}')