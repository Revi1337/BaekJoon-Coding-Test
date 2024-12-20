def solution(N, S, nums):

    def backtracking(n, cnt, sm):
        if n == N:
            if sm == S and cnt >= 1:
                nonlocal answer
                answer += 1
            return

        backtracking(n + 1, cnt + 1, sm + nums[n])
        backtracking(n + 1, cnt, sm)

    answer = 0
    backtracking(0, 0, 0)

    return answer


N, S = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(N, S, nums))
