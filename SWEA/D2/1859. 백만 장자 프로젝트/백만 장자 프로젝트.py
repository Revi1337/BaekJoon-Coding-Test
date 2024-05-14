def solution(idx, N, prices):
    answer = must = 0
    for price in prices[::-1]:
        if price >= must:
            must = price
        else:
            answer += must - price
    return f'#{idx} {answer}'

T = int(input())
for idx in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    print(solution(idx + 1, N, prices))
