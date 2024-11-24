def solution(N, prices):
    max_price = prices[-1]
    answer = 0
    for price in prices[-2::-1]:
        if price > max_price:
            max_price = price
            continue

        answer += max_price - price

    return answer

T = int(input())
for seq in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    print(f'#{seq + 1} {solution(N, prices)}')