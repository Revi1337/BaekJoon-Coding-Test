def solution(N, eggs):

    def backtracking(n, breaked):
        if n == N:
            nonlocal answer
            answer = max(answer, breaked)
            return

        blood, attack = eggs[n]
        if blood == 0:
            backtracking(n + 1, breaked)
        else:
            all_breaked = True
            for idx in range(N):
                if idx == n or eggs[idx][0] == 0:
                    continue
                all_breaked = False
                tblood, attack = eggs[idx]

                eggs[n][0] = max(eggs[n][0] - eggs[idx][1], 0)
                eggs[idx][0] = max(eggs[idx][0] - eggs[n][1], 0)
                backtracking(n + 1, breaked + int(not eggs[idx][0]) + int(not eggs[n][0]))
                eggs[n][0] = blood
                eggs[idx][0] = tblood
            if all_breaked:
                backtracking(n + 1, breaked)

    answer = 0
    backtracking(0, 0)

    return answer

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, eggs))