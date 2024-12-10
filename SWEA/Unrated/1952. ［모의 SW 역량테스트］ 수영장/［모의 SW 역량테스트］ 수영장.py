def solution(day, mon, mon3, year, prices):
    prices = [0] + prices
    answer = 3000 * 12

    def backtracking(n, sm):
        nonlocal answer
        if answer <= sm:
            return

        if n > 12:
            answer = min(answer, sm)
            return

        backtracking(n + 1, sm + day * prices[n])
        backtracking(n + 1, sm + mon)
        backtracking(n + 3, sm + mon3)
        backtracking(n + 12, sm + year)

    backtracking(1, 0)

    return answer

T = int(input())
for seq in range(T):
    day, mon, mon3, year = map(int, input().split())
    prices = list(map(int, input().split()))
    print(f'#{seq + 1} {solution(day, mon, mon3, year, prices)}')