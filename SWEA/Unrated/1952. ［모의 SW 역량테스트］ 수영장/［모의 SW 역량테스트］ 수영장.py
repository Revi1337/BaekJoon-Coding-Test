def solution(day, mon, mon3, year, prices):
    prices = [0] + prices

    D = [0] * 13
    for month in range(1, 13):
        mn = D[month - 1] + prices[month] * day # 일일권
        mn = min(mn, D[month - 1] + mon) # 월간권과 비교
        if month >= 3:
            mn = min(mn, D[month - 3] + mon3)
        if month >= 12:
            mn = min(mn, D[month - 12] + year)

        D[month] = mn

    return D[12]

T = int(input())
for seq in range(T):
    day, mon, mon3, year = map(int, input().split())
    prices = list(map(int, input().split()))
    print(f'#{seq + 1} {solution(day, mon, mon3, year, prices)}')
