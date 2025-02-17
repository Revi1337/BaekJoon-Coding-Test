def solution(N, days):

    def dfs(n, sm):
        if n >= N:
            nonlocal answer
            answer = max(answer, sm)
            return
        if n + days[n][0] <= N:
            dfs(n + days[n][0], sm + days[n][1])
        dfs(n + 1, sm)

    answer = 0
    dfs(0, 0)
    return answer

N = int(input())
days = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, days))