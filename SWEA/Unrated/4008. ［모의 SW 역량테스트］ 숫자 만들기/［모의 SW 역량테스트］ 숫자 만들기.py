def solution(N, opers, nums):

    def backtrack(n, sm):
        if n == N - 1:
            nonlocal mn, mx
            mn, mx = min(mn, sm), max(mx, sm)
            return

        for idx in range(4):
            if opers[idx]:
                opers[idx] -= 1
                if idx == 0:
                    backtrack(n + 1, sm + nums[n + 1])
                elif idx == 1:
                    backtrack(n + 1, sm - nums[n + 1])
                elif idx == 2:
                    backtrack(n + 1, sm * nums[n + 1])
                else:
                    backtrack(n + 1, int(sm / nums[n + 1]))
                opers[idx] += 1

    mn, mx = 1e9, -1e9
    backtrack(0, nums[0])

    return mx - mn

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    opers = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    print(f'#{t} {solution(N, opers, nums)}')
