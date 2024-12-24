def solution(N, M, houses):

    def backtracking(n, cnt, chicks):
        if n == chicken_length:
            if cnt == limit:
                sm_dis = 0
                for hr, hc in homes:
                    mn_dis = 1e9
                    for cr, cc in chicks:
                        mn_dis = min(mn_dis, abs(hr - cr) + abs(hc - cc))
                    sm_dis += mn_dis
                nonlocal answer
                answer = min(answer, sm_dis)
            return

        backtracking(n + 1, cnt + 1, chicks + [[*chickens[n]]])
        backtracking(n + 1, cnt, chicks)

    homes, chickens = [], []
    for row in range(N):
        for col in range(N):
            if houses[row][col] == 2:
                chickens.append([row, col])
            elif houses[row][col] == 1:
                homes.append([row, col])

    home_length, chicken_length = len(homes), len(chickens)
    answer = 1e9
    for limit in range(1, M + 1):
        backtracking(0, 0, [])

    return answer

N, M = map(int, input().split())
houses = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, houses))